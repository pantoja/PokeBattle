from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse

from model_mommy import mommy

from battles.models import Battle


class TestCreateBattleView(TestCase):
    view_name = "battles:create_battle"

    def setUp(self):
        self.creator = mommy.make("users.User")
        self.creator.save()
        self.opponent = mommy.make("users.User")
        self.view_url = reverse(self.view_name)
        self.client = Client()
        self.client.force_login(self.creator)

    def test_create_battle(self):
        post_data = {"user_creator": self.creator.id, "user_opponent": self.opponent.id}
        response = self.client.post(self.view_url, post_data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_created_battle_user_is_the_same_as_the_logged_one(self):
        post_data = {"user_creator": self.creator.id, "user_opponent": self.opponent.id}
        self.client.post(self.view_url, post_data, follow=True)

        creator = Battle.objects.last().user_creator
        opponent = Battle.objects.last().user_opponent
        self.assertEqual((creator, opponent), (self.creator, self.opponent))

    def test_unlogged_user_cant_create_battle(self):
        with self.assertRaises(TypeError):
            post_data = {"user_creator": None, "user_opponent": self.opponent.id}
            self.client.post(self.view_url, post_data, follow=True)

    def test_create_battle_redirects_to_success_url(self):
        post_data = {"user_creator": self.creator.id, "user_opponent": self.opponent.id}
        response = self.client.post(self.view_url, post_data, follow=True)
        self.assertRedirects(
            response,
            "/create-team/1",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_client_is_not_a_field_choice(self):
        response = self.client.get(self.view_url)
        options = response.context["form"].fields["user_opponent"].queryset
        self.assertNotIn(self.client, options)


class TestDetailBattleView(TestCase):
    view_name = "battles:detail_battle"

    def setUp(self):
        self.trainer_1 = mommy.make("users.User")
        self.trainer_2 = mommy.make("users.User")
        self.client = Client()
        self.client.force_login(self.trainer_1)
        self.pokemon_1 = mommy.make("pokemon.Pokemon", id=1)
        self.pokemon_2 = mommy.make("pokemon.Pokemon", id=2)
        self.pokemon_3 = mommy.make("pokemon.Pokemon", id=3)
        self.view_url = reverse(self.view_name, kwargs={"pk": 1})

    def test_detail_battle_successfully(self):
        battle = mommy.make(
            "battles.Battle",
            user_creator=self.trainer_1,
            user_opponent=self.trainer_2,
            settled=True,
            winner=self.trainer_2,
        )

        mommy.make(
            "battles.Team",
            trainer=self.trainer_1,
            battle=battle,
            first_pokemon=self.pokemon_1,
            second_pokemon=self.pokemon_2,
            third_pokemon=self.pokemon_3,
        )

        mommy.make(
            "battles.Team",
            trainer=self.trainer_2,
            battle=battle,
            first_pokemon=self.pokemon_1,
            second_pokemon=self.pokemon_2,
            third_pokemon=self.pokemon_3,
        )

        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)

    def test_user_not_creator_of_active_battle_is_denied(self):
        battle = mommy.make(
            "battles.Battle",
            user_creator=self.trainer_2,
            user_opponent=self.trainer_1,
            settled=False,
        )

        mommy.make(
            "battles.Team",
            trainer=self.trainer_2,
            battle=battle,
            first_pokemon=self.pokemon_1,
            second_pokemon=self.pokemon_2,
            third_pokemon=self.pokemon_3,
        )

        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 302)

    def test_user_not_in_this_battle_is_denied(self):
        trainer_3 = mommy.make("users.User")

        battle = mommy.make(
            "battles.Battle",
            user_creator=self.trainer_2,
            user_opponent=trainer_3,
            settled=True,
            winner=self.trainer_2,
        )

        mommy.make(
            "battles.Team",
            trainer=self.trainer_2,
            battle=battle,
            first_pokemon=self.pokemon_1,
            second_pokemon=self.pokemon_2,
            third_pokemon=self.pokemon_3,
        )

        mommy.make(
            "battles.Team",
            trainer=trainer_3,
            battle=battle,
            first_pokemon=self.pokemon_1,
            second_pokemon=self.pokemon_2,
            third_pokemon=self.pokemon_3,
        )

        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 302)

    def test_allow_user_is_creator_of_active_battle(self):
        battle = mommy.make(
            "battles.Battle",
            user_creator=self.trainer_1,
            user_opponent=self.trainer_2,
            settled=False,
        )
        mommy.make(
            "battles.Team",
            trainer=self.trainer_1,
            battle=battle,
            first_pokemon=self.pokemon_1,
            second_pokemon=self.pokemon_2,
            third_pokemon=self.pokemon_3,
        )
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)


class TestCreateTeamView(TestCase):
    view_name = "battles:create_team"

    def setUp(self):
        self.creator = mommy.make("users.User")
        self.opponent = mommy.make("users.User")
        self.battle = mommy.make(
            "battles.Battle", user_creator=self.creator, user_opponent=self.opponent
        )
        self.client = Client()
        self.client.force_login(self.creator)
        self.view_url = reverse(self.view_name, kwargs={"pk": 1})
        self.pokemon_set = mommy.make("pokemon.Pokemon", attack=50, defense=50, hp=50, _quantity=3)

    def test_user_allowed_to_create_team(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)

    def test_user_not_invited_to_battle_is_redirected(self):
        user_creator = mommy.make("users.User")
        mommy.make(
            "battles.Battle", user_creator=self.opponent, user_opponent=user_creator, settled=False,
        )
        url = reverse(self.view_name, kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertRedirects(
            response,
            "/create-battle/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_user_already_has_team_in_this_battle(self):
        mommy.make(
            "battles.Team", trainer=self.creator, battle=self.battle,
        )
        response = self.client.get(self.view_url)
        message = list(response.context.get("messages"))[0]
        self.assertEqual(
            message.message, "You've chosen your team for this battle. Check your email for results"
        )
        self.assertEqual(response.status_code, 200)

    def test_invite_email_is_sent(self):
        post_data = {
            "trainer": self.creator.id,
            "battle": self.battle.id,
            "pokemon_1": self.pokemon_set[0].id,
            "pokemon_2": self.pokemon_set[1].id,
            "pokemon_3": self.pokemon_set[2].id,
            "order_1": "1",
            "order_2": "2",
            "order_3": "3",
        }
        self.client.post(self.view_url, post_data)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject, f"PokeBattle - {self.creator.email} invited you to a match"
        )


class TestListActiveBattles(TestCase):
    view_name = "battles:active_battles"

    def setUp(self):
        self.trainer_1 = mommy.make("users.User")
        self.trainer_2 = mommy.make("users.User")

        self.client = Client()
        self.client.force_login(self.trainer_1)

        self.view_url = reverse(self.view_name)

    def test_list_active_battles_succesfully(self):
        mommy.make(
            "battles.Battle",
            user_creator=self.trainer_1,
            user_opponent=self.trainer_2,
            settled=False,
        )

        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["battles"])

    def test_settled_battle_is_not_listed(self):
        active_battle = mommy.make(
            "battles.Battle",
            user_creator=self.trainer_1,
            user_opponent=self.trainer_2,
            settled=False,
        )
        settled_battle = mommy.make(
            "battles.Battle",
            user_creator=self.trainer_1,
            user_opponent=self.trainer_2,
            settled=True,
        )

        response = self.client.get(self.view_url)
        battle_list = response.context["battles"]
        self.assertNotIn(settled_battle, battle_list)
        self.assertIn(active_battle, battle_list)


class TestListSettledBattles(TestCase):
    view_name = "battles:settled_battles"

    def setUp(self):
        self.trainer_1 = mommy.make("users.User")
        self.trainer_2 = mommy.make("users.User")

        self.client = Client()
        self.client.force_login(self.trainer_1)

        self.view_url = reverse(self.view_name)

    def test_list_settled_battles_succesfully(self):
        mommy.make(
            "battles.Battle",
            user_creator=self.trainer_1,
            user_opponent=self.trainer_2,
            settled=True,
            winner=self.trainer_1,
        )

        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["battles"])

    def test_active_battle_is_not_listed(self):
        active_battle = mommy.make(
            "battles.Battle",
            user_creator=self.trainer_1,
            user_opponent=self.trainer_2,
            settled=False,
        )
        settled_battle = mommy.make(
            "battles.Battle",
            user_creator=self.trainer_1,
            user_opponent=self.trainer_2,
            settled=True,
        )

        response = self.client.get(self.view_url)
        battle_list = response.context["battles"]
        self.assertNotIn(active_battle, battle_list)
        self.assertIn(settled_battle, battle_list)
