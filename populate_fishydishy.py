import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fishy_dishy_project.settings')

import django
django.setup()
from fishydishy.models import Fish, Recipe

def populate():
    fish = [
        {"name": "Anchovy",
         "type": "oily_fish",
         "sustainability": 3,
         "description": "Small green fish with a silver stripe that gives them a bluish hue. A relative of the herring, they are a short-lived, schooling fish feeding on small fry (recently hatched fish) and plankton at the bottom of the food-chain. As an oily fish, their strong flavour is used to add a kick to many dishes and sauces, including Worcestershire Sauce, and they are widely used in Mediterranean cooking.",
         "image": "static/fish_images/anchovy.jpg",
         "area": "North East & Eastern Central Atlantic, Mediterranean and Black Sea"
         },
        {"name": "Mackerel",
         "type": "oily_fish",
         "sustainability": 3,
         "description": "When cooked the meat is really creamy and is full of omega-3 fatty acids. Mackerel is best eaten fresh and can be grilled, smoked or fried. It's rumoured to improve brain power so an ideal starter fish for the kids! A fast swimming silver and blue striped fish belonging to a group of fish called Scombrids, it's related to tuna. They swim around in huge shoals which feed on small fish and prawns.",
         "image": "static/fish_images/mackerel.jpg",
         "area": "North East Atlantic"
         },
        {"name": "Seabass",
         "type": "white_fish",
         "sustainability": 2,
         "description": "Seabass are thick-set fish with silvery-scales and a rapid swimming predator, prized by anglers and chefs alike. Can be roasted, grilled, baked or barbecued, also be steamed or poached. Good with rosemary, garlic or lemon.",
         "image": "static/fish_images/seabass.jpg",
         "area": "North East Atlantic"
         },
        {"name": "Bream",
         "type": "white_fish",
         "sustainability": 2,
         "description": "Seabream are a group of compact, medium-sized fishes known as Sparidae. Their firm white meat is similar in taste and texture to bass and is ideal for grilling, steaming, baking and pan-frying whole. Black bream or porgy are commonly found in northern European seas and are commercially fished. However the bulk of the seabream in the UK market comes from imports of Mediterranean farmed gilthead bream. Black bream is a pretty inexpensive fish to eat as it's not massively popular despite the fact it's delicious. Its taste is distinctive and on the sweet side so best grilled or stuffed and baked whole (after removing its scales).",
         "image": "static/fish_images/seabream.jpg",
         "area": "North East Atlantic"
         },
        {"name": "Oyster",
         "type": "shell_fish",
         "sustainability": 4,
         "description": "A great choice for special occasions, or a regular treat! Often eaten raw, but can be lightly cooked. They taste like a mouthful of seawater, in fact the French poet Leon-Paul Fargue said eating one was 'like kissing the sea on the lips'. Oysters are rich in zinc and said to have aphrodisiac properties. They should be tightly closed when bought and have a fresh smell when opened. ",
         "image": "static/fish_images/oyster.jpg",
         "area": "North East Atlantic"
         },
        {"name": "Mussels",
         "type": "shell_fish",
         "sustainability": 5,
         "description": "Mussels can be smoked, boiled, steamed, roasted, barbecued or fried in butter or vegetable oil. As with all shellfish, except shrimp, mussels should be checked to ensure they are still alive just before they are cooked; enzymes quickly break down the meat and make them unpalatable or poisonous after dying or uncooked. Some mussels might contain toxins. A simple criterion is that live mussels, when in the air, will shut tightly when disturbed. Open, unresponsive mussels are dead, and must be discarded.",
         "image": "static/fish_images/mussels.jpg",
         "area": "UK"
         },
        {"name": "Brill",
         "type": "flat_fish",
         "sustainability": 3,
         "description": "Sold as whole steaks and fillets and is sometimes used as an alternative to turbot. It is similar to turbot but has slightly smaller flakes and a sweeter taste. Brill belongs to a small family of left-eyed flatfish. It grows relatively fast and generally reaches a certain length faster (at younger ages) than flatfish, such as sole and plaice, in the same areas.",
         "image": "static/fish_images/brill.jpg",
         "area": "North East Atlantic"
         },
        {"name": "Halibut",
         "type": "flat_fish",
         "sustainability": 1,
         "description": "Atlantic halibut can grow up to 8ft long and 4ft wide, is the largest and longest lived of all flatfish, is heavily overfished and listed as an Endangered species so avoid eating! Farmed Atlantic or wild-caught Pacific halibut from the Northeast Pacific and Northwest Atlantic and certified to the Marine Stewardship Council (MSC) standard for responsible fishing are more sustainable options. ",
         "image": "static/fish_images/halibut.jpg",
         "area": "North East Atlantic"
         },
        {"name": "Salmon",
         "type": "oily_fish",
         "sustainability": 3,
         "description": "Salmon is an oily fish rich in Omega 3. It's a good source of Vitamin D, phosphorous and calcium. Fresh salmon may be baked, grilled or poached. It is also canned, pickled (gravadlax) or smoked. It's also used as a substitute for sushi and in sashimi. Generally stocks of wild Atlantic salmon are depleted. There may be several reasons for this. Factors include: marine mortality, linked to ocean climate and productivity; pollution; environmental changes; aquaculture; freshwater habitat deterioration; and impediments to migration routes. Due to their migratory behaviour it is difficult to effectively manage individual populations. ICES scientists recommend that fishing for salmon only takes place in rivers where stocks are at full reproductive capacity or above conservation limits. Avoid eating wild-caught salmon from rivers below these limits.",
         "image": "static/fish_images/salmon.jpg",
         "area": "Varies according to species, but mainly located in the North East Atlantic"
         },
        {"name": "Whitebait",
         "type": "oily_fish",
         "sustainability": 4,
         "description": "Whitebait are tiny, immature, silvery members of the herring group that are typically deep-fried to serve. They are widely thought to be baby herring and are usually sold frozen. The term whitebait is used widely throughout the world, referring to small, usually marine, fishes. It has been reported that whitebait available in the UK is made up mostly of young sprats from the Baltic Sea, but depending on the source, these may be mixed with the young of shad, herrings, sticklebacks, gobies and shrimps.",
         "image": "static/fish_images/whitebait.jpg",
         "area": "North East Atlantic"
         },
        {"name": "Cod",
         "type": "white_fish",
         "sustainability": 3,
         "description": "The most popular cuts are steaks and fillets which can be poached, grilled or baked. It's easy and quick to cook and is traditionally served with parsley sauce and lemon wedges and of course, chips. Cod roe and milt or sperm is also eaten. Cod belongs to a family of fish known as gadoids, which includes species such as haddock, pollack, pouting and ling. The fish is brown to green with spots on the dorsal side with a distinctive lateral line, and a small 'bib' or barbel under its chin which is used to look for food.Cod produce millions of eggs in winter and spring in February to April. ",
         "image": "static/fish_images/cod.jpg",
         "area": "North East Atlantic, Baltic Sea"
         }

    ]

    recipe = [
        {
        "name": "Baja Fish Tacos",
        "description": "The prototypical fish taco originated in Baja California, Mexico, and the preparation referred to in this country as “Baja-style” is similar to what you might find on the Mexican peninsula. It usually involves deep-fried white-fleshed fish, shredded cabbage, and a creamy white sauce.",
        "ingredients": "Vegetable oil, for frying\n 1/4 red cabbage, thinly sliced (about 1 1/2 cups)\n 1/2 cup fresh cilantro, roughly chopped\nJuice of 1 lime, plus wedges for serving\n2 tablespoons honey or agave nectar\n1/2 cup mayonnaise\nKosher salt\n12 corn tortillas\n3/4 cup all-purpose flour\n1/2 teaspoon chili powder\nFreshly ground pepper\n1 1/4 pounds skinless halibut fillet, cut into 2-by-1/2-inch pieces\n1 Hass avocado\n1/2 cup fresh salsa",
        "method": "Heat about 3 inches vegetable oil in a medium pot over medium-low heat until a deep-fry thermometer registers 375 degrees F. Meanwhile, toss the cabbage, cilantro, lime juice, honey and mayonnaise in a bowl. Season the slaw with salt.\nWarm the tortillas in a skillet over medium-low heat or wrap in a damp cloth and microwave 25 seconds. Wrap in a towel to keep warm.\nMix the flour, chili powder, and salt and pepper to taste in a shallow bowl. Dredge the fish in the flour mixture, then fry in batches until golden and just cooked through, 2 to 3 minutes. Transfer with a slotted spoon to a paper-towel-lined plate to drain. Season with salt.\nHalve, pit and slice the avocado. Fill the tortillas with the fish, avocado, slaw and salsa. Serve with lime wedges.",
        "fish": "Halibut",
        "time": 20,
        "serves": 4,
        "image": "recipe_images/fishtacos.jpg"
        },
        {
            "name": "Thai Salmon Fishcakes",
            "description": "Combining the fresh flavours of salmon with the zing of Thai spices, these fish cakes from Thai Taste not only look beautiful but taste amazing too.",
            "ingredients": "450g (1lb) skinless fish fillets (salmon, haddock, etc) cut into chunks, 4 spring onions finely sliced, 1 red chilli, deseeded and finely chopped, 2 tbsp Thai Taste Red Curry Paste, 2 tbsp fresh coriander leaves, 1 tbsp Thai Taste Palm Sugar, 1 tsp Thai Taste Fish Sauce, 1 tbsp fresh lime juice, 50g (2oz) fine green beans, finely sliced, 1 tbsp Thai Taste Rice Bran Oil, for frying",
            "method": "1. Place the fish chunks, spring onions, chilli, curry paste, coriander, palm sugar, fish sauce, lime juice and a pinch of salt in a food processor and blend until finely minced. 2. Transfer to a bowl and stir in the sliced green beans. 3. Divide the mixture into 16 pieces, roll each one into a ball and then flatten into discs. 4. Transfer the fish cakes to a plate, cover with cling film and place in the fridge for 30 minutes to 1 hour to firm up. 5. Heat the oil in a large frying pan and when very hot fry the fish cakes for about 1-2 minute each side, until golden brown and cooked through. Lift out and drain on kitchen paper, then serve with a selection of dipping sauces and a wedge of lime. Garnish with spring onions.",
            "fish": "Salmon",
            "time": 40,
            "serves": 4,
            "image": "recipe_images/fishcakes.jpg"
        },
        {
            "name": "Classic Fried Whitebait and Aioli",
            "description": "The prototypical fish taco originated in Baja California, Mexico, and the preparation referred to in this country as “Baja-style” is similar to what you might find on the Mexican peninsula. It usually involves deep-fried white-fleshed fish, shredded cabbage, and a creamy white sauce.",
            "ingredients": "1 pound tiny whole fish, such as blue anchovies, 1 tablespoon salt (finely ground), 1 cup flour (all-purpose), 1 to 2 cups oil for frying, 4 to 8 lemon wedges",
            "method": "Pick through your fish to look for any that are not pristine. You are looking for ones where the bellies are torn open. This is from enzymes within the fish breaking it down. Toss these and use only those that look nice, smell a bit like cucumbers (not like nasty fish) and that have clear eyes. Mix the salt and flour well. Pour the oil into a cast-iron frying pan or other suitable pan and heat it to 350 F over medium heat. Dust the fish in the seasoned flour and then shake off the excess. Fry in batches, stirring them so they don't stick together, for 2 to 3 minutes. Drain on a fine-meshed rack or paper towels. If you are making a lot of them, heat the oven to warm and place the fish in the oven until you are ready to serve since it is important that you serve whitebait toasty hot.",
            "fish": "Whitebait",
            "time": 15,
            "serves": 4,
            "image": "recipe_images/friedwhitebait.jpg"
        },
        {
            "name": "Roast Brill with Puy Lentils & Shiitake Mushrooms",
            "description": "Dare we say...a brill-iant dish for a dinner party, using firm-textured brill and nutty puy lentils.",
            "ingredients": "250g puy lentils, 2 shallots, 4 tbsp olive oil, 140g shiitake mushrooms, 250g pack cherry or plum tomatoes, 2 tbsp capers, 150ml white wine, 4 x brill (or any other white fish like cod) fillets, skinned - about 140-175g/5-6oz each, 1 small lemon, 1 small bunch of flat-leaf parsley, 140g baby spinach",
            "method": "Heat oven to 200C/fan oven 180C/gas mark 6. Tip the lentils into a pan, and cover with cold water. Bring to the boil and cook for 15-20 mins until they are tender. Drain and keep to one side. Fry the shallots in half the oil in a shallow roasting tray on top of the hob, until softened. Increase the heat and add the mushrooms. Cook for a couple of minutes, until they are colouring around the edges. Remove the tray from the heat, then stir in the cooked lentils, halved tomatoes, capers and wine. Sit the fish on the lentils then top with a couple of slices of lemon and drizzle over the remaining oil. Season everything with flaked sea salt and freshly ground black pepper. Roast for 15 mins – until the fish is cooked through and beginning to go golden on top. Gently lift fish from the tray. Stir the parsley and spinach into lentils, until the spinach starts to wilt. Spoon onto 4 plates, sit the fish on top and serve.",
            "fish": "Brill",
            "time": 50,
            "serves": 4,
            "image": "recipe_images/brilldish.jpg"
        }
    ]

    for item in fish:
        f = add_fish(item["name"], item["type"], item["sustainability"], item["description"], item["image"], item["area"])
        print(format(str(f)))


    for item in recipe:
        r = add_recipe(item["name"], item["description"], item["ingredients"], item["method"], get_fish(item["fish"]), item["time"], item["serves"], item["image"])
        print(format(str(r)))

def add_fish(name, type, sustainability, description, image, area):
    f = Fish.objects.get_or_create(name = name, fishType = type, description = description, sustainability = sustainability, image = image, area = area)
    return f

def get_fish(name):
    fish = Fish.objects.get(name = name)
    return fish


def add_recipe(name, description, ingredients, method, fish, time, serves, image):
    r = Recipe.objects.get_or_create(name = name, description = description, ingredients = ingredients, method = method, fish = fish, time = time, serves = serves, image = image)
    return r

if __name__ == '__main__':
    print("Starting fishy pop script")
    populate()