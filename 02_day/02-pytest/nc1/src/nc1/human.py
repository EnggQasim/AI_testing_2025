class Human:
    def __init__(self, name: str, age: int, height: float, weight: float):
        """
        Initialize a Human instance.
        
        Args:
            name: The name of the human
            age: Age in years
            height: Height in meters
            weight: Weight in kilograms
            
        Raises:
            ValueError: If height is zero or negative, or if weight is negative
        """
        if height <= 0:
            raise ValueError("Height must be greater than zero")
        if weight < 0:
            raise ValueError("Weight cannot be negative")
            
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def get_bmi(self) -> float:
        """Calculate and return the Body Mass Index (BMI)."""
        return self.weight / (self.height ** 2)
    
    def is_adult(self) -> bool:
        """Return True if the human is 18 or older."""
        return self.age >= 18
    
    def introduce(self) -> str:
        """Return a string introduction of the human."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def celebrate_birthday(self) -> None:
        """Increment the age by one year."""
        self.age += 1 