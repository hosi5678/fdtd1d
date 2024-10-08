import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from count_csv_files import count_csv_files
from shell_command import shell_command

# 最大値、最小値のファイルを開く
ey_range_file="./csv_files/ey_range.csv"
pngs_dir="./ey_pngs/"

df=pd.read_csv(ey_range_file,header=None)

# 最大値、最小値の表示
print("ez_max="+str(df.iloc[0].max()))
print("ez_min="+str(df.iloc[1].min()))

# 最大値、最小値の取得
vmax=df.iloc[0].max()
vmin=df.iloc[1].min()

# csv filesのフォルダパス
csv_dir="./ey_timestep/"

# csvのファイル数の取得
timestep = count_csv_files(csv_dir)

# csv fileのfile数の表示
print(str(timestep)+" csv files were found.")

# 出力するフレーム数の入力
timestep = int(input("input timestep number.(>0)"))



for i in range(timestep):
    # figure(全体図)のサイズをfull hdに設定
    fig=plt.figure(figsize=(1920/80,1080/80),dpi=80)

    # 2行1列の1行目
    ax1=fig.add_subplot(2,1,1)

    # 6桁固定のiを作り出す
    fmt_i = '{:06d}'.format(i)
    csv_file=csv_dir+"ey_timestep_"+'{:06d}'.format(i)+".csv"

    # data frameに読み込む
    y_values=pd.read_csv(csv_file,header=0)

    # y_values=df.iloc[0];

    # x軸のデータ（1行目）
    x_values=range(len(y_values));
    
    
    # print(x_values)
    
    # print(y_values)
    # data=df.rows;
    # x=data.length;
    
    ax1.set_title("amplitude of ey",{"fontsize":20})
    
    ax1.set_ylim(top=vmax)
    ax1.set_ylim(bottom=vmin)
    
    ax1.plot(x_values, y_values, linestyle='-', color='b')

    # 2行1列の2行目
    ax2=fig.add_subplot(2,1,2)

    ax2.set_title('Heatmap of Ey',{"fontsize": 20})

    # print("x_values")
    # print(x_values);
    
    # 2行目以降の1列目をy軸の値として取得
    # y_values = df.index[1:]
    
    # print("y_values:"+str(y_values))
    
    # 2行目以降のデータを取得
    # data = df.iloc[1:, 1:]

    # figure(全体図)のサイズを1080を中心とした正方形に設定
    # fig=plt.figure(figsize=(1300/80,1080/80),dpi=80)

    # fig.suptitle('Heatmap of Ey',fontsize=20)

    # heatmapにもx軸を設定する。間隔はxticklabels=5で設定する。
    # vmax,vminの設定
    # cbar(sideのcolorbarはFalseとする)
    heatmap=sns.heatmap(
        y_values.T,
        xticklabels=5,
        yticklabels=5,
        cmap='coolwarm',
        cbar=False,
        center=0.0,
        vmax=vmax,
        vmin=vmin
    )

    # x_tick_positions = range(0, len(x_values), 5)
    # y_tick_positions = range(0, len(y_values), 5)

    # heatmap.set_xticks(x_tick_positions)
    # heatmap.set_yticks(y_tick_positions)

    # heatmap.set_xticklabels(x_values[x_tick_positions],fontsize=18)
    # heatmap.set_yticklabels(y_values[y_tick_positions],fontsize=10)

    # heatmap.invert_yaxis()

    heatmap.set_xlabel('x position' , {"fontsize":20})

    heatmap.set_ylabel('y position' , {"fontsize":20} )

    plt.suptitle("timestep="+str(i),fontsize=25)

    # ファイルを保存
    plt.savefig(pngs_dir+"ey_timestep_"+fmt_i+".png")

    # saveの表示
    if(i%50==0):
        print(pngs_dir+"ey_timestep_"+fmt_i+".png"+"/"+str(timestep)+" was created.")

    # csv fileの削除
    # os.unlink(csv_file)

    # メモリの解放
    plt.clf()
    plt.close()
