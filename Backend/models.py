from pydantic import BaseModel
#pydantic is a data validation and settings management library
class EventInput(BaseModel): #basemodel is coreclass we need to inherit to define schemas 
    tab_url: str
    title: str
    scroll_depth: float
