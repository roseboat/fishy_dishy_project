import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fishy_dishy_project.settings')

import django
django.setup()
from fishydishy.models import Fish

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
         "description": "Mussels can be smoked, boiled, steamed, roasted, barbecued or fried in butter or vegetable oil. As with all shellfish, except shrimp, mussels should be checked to ensure they are still alive just before they are cooked; enzymes quickly break down the meat and make them unpalatable or poisonous after dying or uncooked.[citation needed] Some mussels might contain toxins.[18] A simple criterion is that live mussels, when in the air, will shut tightly when disturbed. Open, unresponsive mussels are dead, and must be discarded.",
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
         }
    ]

    for item in fish:
        f = add_fish(item["name"], item["type"], item["sustainability"], item["description"], item["image"], item["area"])
        print(format(str(f)))


def add_fish(name, type, sustainability, description, image, area):
    f = Fish.objects.get_or_create(name = name, fishType = type, description = description, sustainability = sustainability, image = image, area = area)
    return f

if __name__ == '__main__':
    print("Starting fishy pop script")
    populate()