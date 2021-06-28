import const
import random

def nextMove( team_index, pos_table, scores ):
  result = "stay"
  variable = random.randint(0, 2)

  if variable == 0:
    result = "up"
  elif variable == 1:
    result = "down"
  else:
    result = "stay"

  return result

def showSituation( pos_table, scores ):
  for agent in range( len(pos_table) ):
    print( "[Group {:0=2}] ".format( agent+1 ), end="" )
    for turn in range( len( pos_table[agent] ) ):
      print( pos_table[agent][turn], end=" " )
    print( " (Score: {})".format( scores[agent] ) )
  print()

def showPopulation( pos_table ):
  population = calculatePopulation( pos_table )
  print( "Population: {}".format( population ) )

def calculatePopulation( pos_table ):
  population = [0 for i in range( const.n_rows )]
  for agent in range( len(pos_table) ):
    population[ pos_table[agent][-1] ] += 1
  return population

def currentPos( team_index, pos_table ):
  return pos_table[team_index][-1]
