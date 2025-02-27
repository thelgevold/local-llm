from pydantic import Field

def get_country_border_info(bordering_countries: list[str] = Field(description="bordering countries that share a physical border")):
    """Usfeful for getting a list of countries that share a physical border with the country"""
    
    bordering_countries.sort()
    
    return  {"bordering_countries": bordering_countries}

def get_country_prime_minister(prime_minister: list[str] = Field(description="the prime minister of the country")) -> str:
    """Usfeful for getting the prime minister the country"""
    
    return  {"prime_minister": prime_minister}
