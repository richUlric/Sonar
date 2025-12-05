import unittest
from src.game_logic import GameLogic

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()

    def test_initial_state(self):
        self.assertEqual(self.game.current_player, "X")
        self.assertEqual(self.game.board, [['' for _ in range(3)] for _ in range(3)])
        self.assertIsNone(self.game.winner)
        self.assertFalse(self.game.is_draw)

    def test_on_click(self):
        self.assertTrue(self.game.on_click(0, 0))
        self.assertEqual(self.game.board[0][0], "X")
        self.assertEqual(self.game.current_player, "O")
        self.assertFalse(self.game.on_click(0, 0)) # Click on non-empty cell

    def test_win(self):
        self.game.on_click(0, 0) # X
        self.game.on_click(1, 0) # O
        self.game.on_click(0, 1) # X
        self.game.on_click(1, 1) # O
        self.game.on_click(0, 2) # X
        self.assertTrue(self.game.check_win("X"))
        self.assertEqual(self.game.winner, "X")

    def test_win_anti_diag(self):
        self.game.on_click(0, 2) # X
        self.game.on_click(1, 0) # O
        self.game.on_click(1, 1) # X
        self.game.on_click(1, 2) # O
        self.game.on_click(2, 0) # X
        self.assertTrue(self.game.check_win("X"))
        self.assertEqual(self.game.winner, "X")

    def test_draw(self):
        # Séquence de jeu menant à un match nul
        self.game.on_click(0, 0) # X
        self.game.on_click(1, 1) # O
        self.game.on_click(0, 1) # X
        self.game.on_click(0, 2) # O
        self.game.on_click(2, 0) # X
        self.game.on_click(1, 0) # O
        self.game.on_click(1, 2) # X
        self.game.on_click(2, 2) # O
        self.game.on_click(2, 1) # X - C'est le dernier coup, qui remplit le plateau

        self.assertIsNone(self.game.winner) # Personne n'a gagné
        self.assertTrue(self.game.is_draw)  # La partie est un match nul

    def test_click_after_game_over(self):
        # Win condition
        self.game.on_click(0, 0) # X
        self.game.on_click(1, 0) # O
        self.game.on_click(0, 1) # X
        self.game.on_click(1, 1) # O
        self.game.on_click(0, 2) # X
        # Game is won by X, further clicks should be ignored
        self.assertFalse(self.game.on_click(2, 2))

if __name__ == '__main__':
    unittest.main()
