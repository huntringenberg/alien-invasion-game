class GameStats:
    """Track statistics for alien invasion."""

    def __init__(self, ai_game):
        """Initialize stats object."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can be changed during the game."""
        self.ship_left = self.settings.ship_limit

