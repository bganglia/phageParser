from django.test import TestCase
from models import Organism,  Repeat, Spacer, SpacerRepeatPair

class OrganismTestCase(TestCase):
    """This class contains a test suite for the Organism model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.organism_name = "Organism Name"
        self.accession_number = "NC_000000"
        self.organism = Organism(name=self.organism_name, accession=self.accession_number)

    def test_model_can_create_an_organism(self):
        """Test the organism model can create an organism."""
        old_count = Organism.objects.count()
        self.organism.save()
        new_count = Organism.objects.count()
        self.assertNotEqual(old_count, new_count)
