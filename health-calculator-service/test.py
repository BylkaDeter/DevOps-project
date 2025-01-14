import unittest
from health_utils import calculate_bmi, calculate_bmr


class TestHealthUtils(unittest.TestCase):
    """Tests unitaires pour les fonctions utilitaires."""

    def test_calculate_bmi(self):
        """Tester la fonction de calcul du BMI."""
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)
        self.assertAlmostEqual(calculate_bmi(1.60, 50), 19.53, places=2)

    def test_calculate_bmr(self):
        """Tester la fonction de calcul du BMR."""
        # Homme
        self.assertAlmostEqual(calculate_bmr(175, 70, 25, "male"), 1724.05, places=2)
        # Femme
        self.assertAlmostEqual(calculate_bmr(165, 60, 30, "female"), 1383.68, places=2)


if __name__ == "__main__":
    unittest.main()
