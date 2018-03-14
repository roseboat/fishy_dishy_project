from django.test import TestCase
from fishydishy.models import Recipe
from fishydishy.models import Fish
from django.core.urlresolvers import reverse

def add_recipe(name, description, ingredients, method, fish, time, serves, image):
    r = Recipe.objects.get_or_create(name=name, description=description, ingredients=ingredients, method=method,
                                     fish=fish, time=time, serves=serves, image=image)
    return r


#model tests for Recipes
class RecipeMethodTest(TestCase):
    
    # this test checks that the minimum preparation time will be above 0
    def test_ensure_time_is_above_zero_minutes(self):

        newFish= Fish(name='Salmon',  fishType='Oily', description='None', area='The Sea', sustainability=3)
        newFish.save()
        
        recipe= Recipe(name='Fish', fish=newFish, serves=1, time=0)
        recipe.save()
        
        self.assertEqual((recipe.time >0), True)

    # this test checks that the minimum number of serving will be at least 1
    def test_ensure_serve_is_at_least_for_1(self):

        newFish= Fish(name='Salmon',  fishType='Oily', description='None', area='The Sea', sustainability=3)
        newFish.save()
        
        recipe= Recipe(name='Fish', fish=newFish, serves=0, time=0)
        recipe.save()
        
        self.assertEqual((recipe.serves >0), True)

    # this test checks if an appropriate slug line is created
    def test_url_slug_line_is_valid(self):

        newFish= Fish(name='Salmon',  fishType='Oily', description='None', area='The Sea', sustainability=3)
        newFish.save()
        
        recipe= Recipe(name='Fishy Dishy Special', fish=newFish, serves=0, time=0)
        recipe.save()

        self.assertEqual (recipe.slug, 'fishy-dishy-special')

# views test for Recipes
class RecipeViewTests(TestCase):

    def test_view_with_no_recipes(self):
        # Check for no recipes

        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"")
        self.assertQuerysetEqual(response.context['recipeList'], [])


    def test_view_with_recipes(self):
        #Check to make sure recipes are being added to database, loaded page contains "smoked fish" recipe
        # and number of categories equals 1

        newFish = Fish (name='Halibut', fishType = 'oily', description = 'big fish', sustainability = 5, area = "UK")
        newFish.save()

        add_recipe('smoked fish', 'fasfa', 'adadawda', 'wadadaw', newFish, 20,2, 'static/recipe_images/fishtacos.jpg')

        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "smoked fish")

        num_recipes = len(response.context['recipeList'])
        self.assertEqual(num_recipes, 1)
