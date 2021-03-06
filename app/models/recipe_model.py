from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

@dataclass
class RecipeModel(db.Model):
    id:int
    name:str
    method_of_preparation:str

    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    method_of_preparation = Column(String,nullable=False)

    ingredients = relationship("IngredientModel",backref="recipe",uselist=True)


    mandatory_data = {
        "name":str,
        "method_of_preparation":str,
    }

    def serialize(self):
        return{
            "recipeId":self.id,
            "name":self.name,
            "method_of_preparation":self.method_of_preparation,
            "ingredients":self.ingredients
        }