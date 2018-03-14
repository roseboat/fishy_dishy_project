from django.test import TestCase
from fishydishy.models import Recipe
from fishydishy.models import Fish

# this test checks that the minimum preparation time will be above 0
class RecipeTimeTest(TestCase):
    def test_ensure_time_is_above_zero_minutes(self):

        newFish= Fish(name='Salmon',  fishType='Oily', description='None', area='The Sea', sustainability=3)
        newFish.save()
        
        recipe= Recipe(name='Fish', fish=newFish, serves=1, time=0)
        recipe.save()
        
        self.assertEqual((recipe.time >0), True)

# this test checks that the minimum number of serving will be at least 1
class RecipeServeTest(TestCase):
    def test_ensure_serve_is_at_least_for_1(self):

        newFish= Fish(name='Salmon',  fishType='Oily', description='None', area='The Sea', sustainability=3)
        newFish.save()
        
        recipe= Recipe(name='Fish', fish=newFish, serves=0, time=0)
        recipe.save()
        
        self.assertEqual((recipe.serves >0), True)
