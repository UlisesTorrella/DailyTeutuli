
from Reader import Reader

from datetime import datetime


# Monday    
reader = Reader(test=False)
results = reader.update_leaderboard()
reader.print_podium(results)

