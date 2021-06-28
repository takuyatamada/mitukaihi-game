import const
import random
import csv
import random_strategy as r_s
import simple_strategy as simple_s
# import group20A
# import group20B
# import group20C
# import group20D
# import group20E
# import group20F
# import group20G
# import group20H
# import group20I
# import group20J
# import group20K
# import group20L
# import group20M
# import group20N
# import group20O

const.n_columns = 11
const.n_rows = 5

class GameEngine:
  agents = []
  pos_table = []
  scores = []
  total_scores = []

  def __init__( self ):
    # team registration
    for i in range(5):
      self.agents.append( r_s )
    for i in range(5):
      self.agents.append( simple_s )

    # initialization of situations
    self.pos_table = [ [-1000] for i in range( len(self.agents) ) ]
    self.scores = [ 0 for i in range( len(self.agents) ) ]
    self.total_scores = [ 0 for i in range( len(self.agents) ) ]


  def playGames( self, n_games ):
    for i in range( n_games ):
      print( "----- Game {} -----".format( i+1 ) )
      self.playOneGame()
      self.saveLog( i )

  def playOneGame( self ):
    self.initializeGame()

    for i in range( 10 ):
      if i == 0:
        print( "Initial positions" )
      else:
        print( "Turn {}".format( i ) )
      self.showSituation()

      # send pos_table to agent and receive information from agent
      decision = []
      for team in range( len(self.agents) ):
        next_move = self.handler( self.agents[team].nextMove, team, self.pos_table, self.scores )
        decision.append( next_move )

      # update agent positions
      for agent in range( len(self.agents) ):
        current_pos = self.pos_table[agent][i]
        if decision[agent] == "up":
          next_pos = current_pos - 1
          if next_pos < 0:
            next_pos = const.n_rows - 1
        elif decision[agent] == "down":
          next_pos = current_pos + 1
          if next_pos == const.n_rows:
            next_pos = 0
        else: # decision[agent] == "stay" and others
          next_pos = current_pos
        self.pos_table[agent].append( next_pos )

      # reward agents
      population = [0 for i in range( const.n_rows )]
      for agent in range( len(self.agents) ):
        population[ self.pos_table[agent][-1] ] += 1
      for agent in range( len(self.agents) ):
        if population[ self.pos_table[agent][-1] ] <= 2:
          self.scores[agent] += 1
          self.total_scores[agent] += 1

    print( "Game finished.")
    self.showSituation()

  def saveLog( self, n_games ):
    with open( "log.csv", "a+", newline="" ) as f:
      writer = csv.writer(f)
      if f.tell() == 0:
        init_row = []
        init_row.append("Game Index")
        init_row.append("Group Index")
        init_row.append("Strategy")
        for turn in range( len( self.pos_table[0] ) ):
          init_row.append("Turn "+str(turn))
        init_row.append("Score")
        init_row.append("Total score")
        writer.writerow(init_row)

      for num in range( len(self.agents) ):
        l = []
        l.append( str(n_games+1) )
        l.append( str(num) )
        l.append( self.agents[num].__name__ )
        for turn in range( len( self.pos_table[num] ) ):
          l.append( self.pos_table[num][turn] )
        l.append( str(self.scores[num]) )
        l.append( str(self.total_scores[num]))

        writer.writerow(l)
    return

  def showSituation( self ):
    for agent in range( len(self.pos_table) ):
      print( "[Group Index {:0=2}] ".format( agent+1 ), end="" )
      for turn in range( len( self.pos_table[agent] ) ):
        print( self.pos_table[agent][turn], end=" " )
      print( " (Score: {})".format( self.scores[agent] ), end=" " )
      print( " (Total Score: {})".format( self.total_scores[agent] ) )
    print()

  def handler( self, func, *args ):
    return func( *args )

  def initializeGame( self ):
    self.pos_table = [ [-1000] for i in range( len(self.agents) ) ]
    self.scores = [ 0 for i in range( len(self.agents) ) ]
    for agent in range( len(self.pos_table) ):
      self.pos_table[agent][0] = random.randint( 0, const.n_rows-1 )
    return
