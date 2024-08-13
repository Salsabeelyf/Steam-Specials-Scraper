from dataclasses import dataclass

@dataclass
class Game:
    title: str
    link_to_thumbnail: str
    category_tags: list
    rating: str
    no_of_reviews: int
    original_price: float
    discounted_price: float
    discount_percent: int