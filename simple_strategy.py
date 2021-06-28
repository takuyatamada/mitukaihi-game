import random
import const # constant values are defined in game_engine.py

def nextMove( team_index, pos_table, scores ):
  result = "stay"

  pos_current = pos_table[team_index][-1]
  pos_up   = (pos_current + const.n_rows - 1) % const.n_rows
  pos_down = (pos_current + const.n_rows + 1) % const.n_rows

  pop = calculatePopulation(pos_table)

  if (pop[pos_up]+1) < (pop[pos_current]-1) and (pop[pos_up]+1) < pop[pos_down]:
    result = "up"
  elif (pop[pos_down]+1) < (pop[pos_current]-1) and (pop[pos_down]+1) < pop[pos_up]:
    result = "down"
  else:
    result = "stay"

  return result

def calculatePopulation( pos_table ):
  population = [0 for i in range( const.n_rows )]
  for agent in range( len(pos_table) ):
    population[ pos_table[agent][-1] ] += 1
  return population
