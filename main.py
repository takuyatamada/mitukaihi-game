import sys
import game_engine

def main():
  ge = game_engine.GameEngine()

  if len(sys.argv) == 1:
      ge.playGames( 1 )
  else:
      ge.playGames( int(sys.argv[1]) )

  return 0

if __name__ == '__main__':
  main()
