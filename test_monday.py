
from Reader import Reader

from datetime import datetime


# Monday    
reader = Reader(test=True)
results = reader.update_leaderboard()
reader.print_podium(results)

