import const
import random
#以下二つをimport
import csv
import pprint



def nextMove( team_index, pos_table, scores ):

#相手チームの過去の行動を分析し次の行動を予測することを重視したプログラムです。
#何か不具合があれば玉田(sca00174@edu.osakafu-u.ac.jp)まで連絡お願いします
#試合を始める前にdataA.csvの中身を空にして頂きたいです。


#相手チームのチームインデックス、移動まえの状態に置ける、当該チームの状況。を出力していく
#各試合の一番最初のアクションの際には実行しない
#このif字下げできてるか心配
  if len(pos_table[0])!=1:

      #total_positionに一ゲーム前の全体のポジションを代入
      total_position = [0]*5
      #下の15はチーム数、変更あるならここをいじる
      for i in range(15):
          #print(pos_table[i][len(pos_table[0])-2])
          total_position[pos_table[i][len(pos_table[0])-2]]+=1
      #print(total_position)
      with open('dataA.csv', 'a') as f:
      #with open('data.csv') as f:
          #print(f.read())
          writer=csv.writer(f)
          for i in range(1,15):
              #まずはチームインデックスを出力
              #print("i=",i)
              #int変数を出力する方法
              list = []
              #writer.writerow(str(i))
              list.append(i)
              writer.writerow(list)
              #次に移動まえにそのチームが何番のますにいたかをpositionに代入
              #len(pos_table[0])-1で
              position = pos_table[i][len(pos_table[0])-2]
              #第len(pos_table[0])-1での全体図が欲しい。
              #→total_positionに保存済み

              #移動前のポジションについて。各チームからみて同じマスにいるチーム数→team_position[0],
              #一つ上のマスにいるチーム数をteam_position[1],ちなみにif文の分岐で境界を超えている。
              #同様に二つ上のマスにいるチーム数をteam_position[2],3つ、4つと入れていった。
              team_position = [0]*5
              team_position[0]=total_position[position]
              if position<1:
                  next_position=position+4
              else:
                  next_position=position-1
              team_position[1]=total_position[next_position]

              if position<2:
                  next_position=position+3
              else:
                  next_position=position-2
              team_position[2]=total_position[next_position]

              if position<3:
                  next_position = position+2
              else:
                  next_position = position-3
              team_position[3]=total_position[next_position]

              if position <4:
                  next_position = position+1
              else:
                  next_position = position-4
              team_position[4] = total_position[next_position]
              writer.writerow(team_position)
              #print(team_position[0])
              #team_position終了
            #  print("pos_table",type(pos_table[0][0]))

              #次に直前の移動で各チームがどう動いたかを記録
              #upを1→0、stayを0→1、downを-1→2としてmoveに代入

              #移動前が0のマス、移動後が4のマスならupになる
              if pos_table[i][len(pos_table[0])-2]==0 and pos_table[i][len(pos_table[0])-1]==4:
                move=0
              #移動前が4のマス、移動後が0のマスならdownしていることになる。
              elif pos_table[i][len(pos_table[0])-2]==4 and pos_table[i][len(pos_table[0])-1]==0:
                move=2
              elif pos_table[i][len(pos_table[0])-1]>pos_table[i][len(pos_table[0])-2]:
                move=2
              elif  pos_table[i][len(pos_table[0])-1]==pos_table[i][len(pos_table[0])-2]:
                move = 1
              else:
                move = 0

              #print(move)
              list2 = []
              list2.append(move)
              #writer.writerow(str(move))
              #print(type(list2[0]))
              writer.writerow(list2)
      f.close()

  #まずnow_total_positionに現在各マスにいるチーム数を入れていく
  #
  now_total_position = [0]*5
  #下の15はチーム数、変更あるならここをいじる
  for i in range(15):
      #print(pos_table[i][len(pos_table[0])-2])
      now_total_position[pos_table[i][len(pos_table[0])-1]]+=1

  #now_my_position　に自分のいるますを代入
  now_my_position = pos_table[0][len(pos_table[0])-1]

  #現在の状況から確実に点数を取れる行動が存在するならそれを選択する。
  staycount=0
  upcount=0
  downcount=0
  if now_my_position==0:
    staycount = now_total_position[1]+now_total_position[0]+now_total_position[4]
    upcount= now_total_position[3]+now_total_position[4]+now_total_position[0]
    downcount=now_total_position[0]+now_total_position[1]+now_total_position[2]
  elif now_my_position==1:
    staycount=now_total_position[0]+now_total_position[1]+now_total_position[2]
    upcount=now_total_position[1]+now_total_position[0]+now_total_position[4]
    downcount=now_total_position[1]+now_total_position[2]+now_total_position[3]
  elif now_my_position==2:
    staycount=now_total_position[1]+now_total_position[2]+now_total_position[3]
    upcount=now_total_position[0]+now_total_position[1]+now_total_position[2]
    downcount=now_total_position[2]+now_total_position[3]+now_total_position[4]
  elif  now_my_position==3:
    staycount=now_total_position[2]+now_total_position[3]+now_total_position[4]
    upcount=now_total_position[1]+now_total_position[2]+now_total_position[3]
    downcount= now_total_position[1]+now_total_position[0]+now_total_position[4]
  elif  now_my_position==4:
    staycount= now_total_position[3]+now_total_position[4]+now_total_position[0]
    upcount=now_total_position[2]+now_total_position[3]+now_total_position[4]
    downcount = now_total_position[1]+now_total_position[0]+now_total_position[4]
  #print("now_total_position",now_total_position)
  #print("stay=#{0},up=%d#{1},down=#{2}",staycount,upcount,downcount)

  #この下の値、3未満なら確実に点貰えるように動けるけど、現実的に満たさない。
  if staycount<3:
    return 'stay'
  elif upcount<3:
    return 'up'
  elif  downcount<3:
    return 'down'


  #ここからファイルの読み込みに入っていく
  #整数のまま読み込みできない、改行文字とかが入るのか。
  next_team_move=[0]*5
  for i in range(1,15):
    #now_opo_positionに現在のiチームの位置を入れる
    now_opo_position=pos_table[i][len(pos_table[0])-1]
    next_move=1

    three_counter = 0
    result_point=[0]*3
    with open('dataA.csv', encoding='utf-8-sig') as f:
    #with open('dataA.csv') as f:

      reader = csv.reader(f)

      now_team_position = [0]*5
      now_team_position[0]=now_total_position[now_opo_position]
      if now_opo_position<1:
          next_position=now_opo_position+4
      else:
          next_position=now_opo_position-1
      now_team_position[1]=now_total_position[next_position]

      if now_opo_position<2:
          next_position=now_opo_position+3
      else:
          next_position=now_opo_position-2
      now_team_position[2]=now_total_position[next_position]

      if now_opo_position<3:
          next_position = now_opo_position+2
      else:
          next_position = now_opo_position-3
      now_team_position[3]=now_total_position[next_position]

      if now_opo_position <4:
          next_position = now_opo_position+1
      else:
          next_position = now_opo_position-4
      now_team_position[4] = now_total_position[next_position]
      #print("iチームのnow_team_positionの値",i,now_team_position)


      #next_up,next_stay,next_downにiチームの次の行動の評価値をいれる
      '''
      next_up=0
      next_stay=0
      next_down=0
      '''


      #下のfor文を回していくときに、三行セットに考える
      for row in reader:
        #print(row)
        data = []
        #q=row.split
        #print("dataの中身はきます")
        for j in range(len(row)):
          data.append(int(row[j]))
          #print("data=",data)


        if three_counter%3==0 and data[0]==i:

          #print("i=",i)
          #下のnextは上のreaderと連携するよ
          h=next(csv.reader(f))
          #print("three_counte]r",three_counter)
          #team_stateにteam_positionの値を入れる
          team_state=[]
          for k in range(len(h)):
            team_state.append(int(h[k]))
          #print("i,team_state",i,team_state)
          value=100
          value -= (6*abs(team_state[0]-now_team_position[0])+ 4*abs(team_state[1]-now_team_position[1]) + 4*abs(team_state[4]-now_team_position[4]) + abs(team_state[2]-now_team_position[2]) + abs(team_state[3]-now_team_position[3]))
          #print("i,value素点",value,i)
          if value==100:
            value*=18
          elif value>95:
            value*=8
          elif value>88:
            value*=3
          elif value>75:
            value//=2
          elif value<75:
            value//=10

          #print("value",value)
          n=next(csv.reader(f))
          team_result = []
          team_result.append(int(n[0]))
          #print("team_result",team_result)
          result_point[team_result[0]]+=value

          three_counter+=2
        three_counter+=1

        #len(q)で配列数を取り出す
      #  data.append(q)
        #print(data)



      '''
      for row in reader:
        if row[0]==i:
          print(row[0])
          h = next(csv.reader(f))
          h = next(csv.reader(f))
        else:
          h = next(csv.reader(f))
          h = next(csv.reader(f))
      '''
    f.close()
    #up,stay,down同じ値ならstayと仮定、基本的に迷ったらstayするようにする。
    '''
    if result_point[0]==result_point[1] and result_point[0]==result_point[2] and result_point[1]==result_point[2]:
      next_move=1
    elif  result[0]
    '''


    #print("index,result_point",i,result_point)
    if result_point[0]>result_point[1] and result_point[0]>result_point[2]:
      next_move=0
    elif result_point[1]>result_point[0] and result_point[1]>result_point[2]:
      next_move=1
    elif result_point[2]>result_point[0] and result_point[2]>result_point[1]:
      next_move=2

    next_opo_position=0
    if now_opo_position==0 and next_move==0:
      next_opo_position=4
    elif  now_opo_position==4 and next_move==2:
      next_opo_position=0
    elif next_move==0:
      next_opo_position=now_opo_position-1
    elif next_move==2:
      next_opo_position=now_opo_position+1
    else:
      next_opo_position=now_opo_position
    next_team_move[next_opo_position]+=1
  #print("next_team_move",next_team_move)

  omoria=14
  omorib=2

  if now_my_position==0:
    upkitaiti  =next_team_move[4]*omoria+next_team_move[3]*omorib+next_team_move[0]*omorib
    staykitaiti=next_team_move[0]*omoria+next_team_move[4]*omorib+next_team_move[1]*omorib
    downkitaiti=next_team_move[1]*omoria+next_team_move[0]*omorib+next_team_move[2]*omorib
  elif now_my_position==1:
    upkitaiti  =next_team_move[0]*omoria+next_team_move[4]*omorib+next_team_move[1]*omorib
    staykitaiti=next_team_move[1]*omoria+next_team_move[0]*omorib+next_team_move[2]*omorib
    downkitaiti=next_team_move[2]*omoria+next_team_move[1]*omorib+next_team_move[3]*omorib
  elif now_my_position==2:
    upkitaiti  =next_team_move[1]*omoria+next_team_move[0]*omorib+next_team_move[2]*omorib
    staykitaiti=next_team_move[2]*omoria+next_team_move[1]*omorib+next_team_move[3]*omorib
    downkitaiti=next_team_move[3]*omoria+next_team_move[2]*omorib+next_team_move[4]*omorib
  elif now_my_position==3:
    upkitaiti  =next_team_move[2]*omoria+next_team_move[1]*omorib+next_team_move[3]*omorib
    staykitaiti=next_team_move[3]*omoria+next_team_move[2]*omorib+next_team_move[4]*omorib
    downkitaiti=next_team_move[4]*omoria+next_team_move[3]*omorib+next_team_move[0]*omorib
  elif now_my_position==4:
    upkitaiti  =next_team_move[3]*omoria+next_team_move[2]*omorib+next_team_move[4]*omorib
    staykitaiti=next_team_move[4]*omoria+next_team_move[3]*omorib+next_team_move[0]*omorib
    downkitaiti=next_team_move[0]*omoria+next_team_move[4]*omorib+next_team_move[1]*omorib


  if upkitaiti<staykitaiti and upkitaiti<downkitaiti:
    return 'up'
  elif staykitaiti<upkitaiti and staykitaiti<downkitaiti:
    return 'stay'
  elif downkitaiti<upkitaiti and downkitaiti<staykitaiti:
    return 'down'
  elif upkitaiti==staykitaiti and upkitaiti<downkitaiti:
    return 'up'
  elif upkitaiti==downkitaiti and upkitaiti<staykitaiti:
    variable = random.randint(0, 1)
    if variable == 0:
      return 'up'
    else:
      return 'down'
  elif downkitaiti==staykitaiti and downkitaiti<upkitaiti:
    return 'down'
  '''
  with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
      print(row)
      h = next(csv.reader(f))
      h = next(csv.reader(f))
  '''
  #print("ランダムを使用")
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
