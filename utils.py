# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
import re


def examine(filename, outdir='results'):
    # 讀取 excel 資料，跳掉前面十行
    #df = pd.read_excel("轉換前資料.xlsx",skiprows=10)
    df = pd.read_csv(filename, sep='\t', skiprows=10)

    prefix = re.split(r'[\\ /.]', filename)[-2] 

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    # 讀取最大值及最小值
    vbr_max = float(df['VBR'][1])
    vbr_min = float(df['VBR'][2])
    vf1_max = float(df['VF1'][1])
    vf1_min = float(df['VF1'][2])
    vf2_max = float(df['VF2'][1])
    vf2_min = float(df['VF2'][2])
    ir_40v_max = float(df['IR_40V'][1])
    ir_40v_min = float(df['IR_40V'][2])
    vf3_max = float(df['VF3'][1])
    vf3_min = float(df['VF3'][2])

    # 刪掉前面三行
    df = df.drop([0,1,2])

    # 將資料轉換成數值型態
    df['X']=df['X'].astype(int)
    df['Y']=df['Y'].astype(int)
    df['VBR']=df['VBR'].astype(float)
    df['VF1']=df['VF1'].astype(float)
    df['VF2']=df['VF2'].astype(float)
    df['IR_40V']=df['IR_40V'].astype(float)
    df['VF3']=df['VF3'].astype(float)

    # 計算 pivot table
    vbr = df.pivot(index='Y', columns='X', values='VBR')
    vf1 = df.pivot(index='Y', columns='X', values='VF1')
    vf2 = df.pivot(index='Y', columns='X', values='VF2')
    ir_40v = df.pivot(index='Y', columns='X', values='IR_40V')
    vf3 = df.pivot(index='Y', columns='X', values='VF3')

    # 計算正常與否的布林值
    vbr_b = (vbr > vbr_min) & (vbr < vbr_max) 
    vf1_b = (vf1 > vf1_min) & (vf1 < vf1_max) 
    vf2_b = (vf2 > vf2_min) & (vf2 < vf2_max) 
    ir_40v_b = (ir_40v > ir_40v_min) & (ir_40v < ir_40v_max) 
    vf3_b = (vf3 > vf3_min) & (vf3 < vf3_max) 

    # 畫出 VBR 彩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(vbr)
    plt.title(prefix + ' VBR COLOR')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-VBR'))
    plt.close(fig)

    # 畫出 VBR 正常與否的兩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(vbr_b)
    plt.title(prefix + ' VBR BW')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-VBR_BW'))
    plt.close(fig)

    # 畫出 VF1 彩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(vf1)
    plt.title(prefix + ' VF1 COLOR')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-VF1'))
    plt.close(fig)

    # 畫出 VF1 正常與否的兩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(vf1_b)
    plt.title(prefix + ' VF1 BW')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-VF1_BW'))
    plt.close(fig)

    # 畫出 VF2 彩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(vf2)
    plt.title(prefix + ' VF2 COLOR')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-VF2'))
    plt.close(fig)

    # 畫出 VF2 正常與否的兩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(vf2_b)
    plt.title(prefix + ' VF2 BW')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-VF2_BW'))
    plt.close(fig)

    # 畫出 IR_40V 彩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(ir_40v)
    plt.title(prefix + ' IR_40V COLOR')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-IR_40V'))
    plt.close(fig)

    # 畫出 IR_40V 正常與否的兩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(ir_40v_b)
    plt.title(prefix + ' IR_40V BW')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-IR_40V_BW'))
    plt.close(fig)

    # 畫出 VF3 彩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(vf3)
    plt.title(prefix + ' VF3 COLOR')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-VF3'))
    plt.close(fig)

    # 畫出 VF3 正常與否的兩色圖
    fig = plt.figure(figsize=(20,20))
    ax = sns.heatmap(vf3_b)
    plt.title(prefix + ' VF3 BW')
    plt.savefig('{}/{}{}.jpg'.format(outdir, prefix, '-VF3_BW'))
    plt.close(fig)

if __name__=="__main__":
    # 將 logs 目錄底下的檔案都讀進來
    files = []
    for file in os.listdir("logs"):
        if file.endswith(".log"):
            files.append(os.path.join("logs", file))

    # 檢查每一個檔案內的內容
    try:
        for file in files:
            examine(file)
    except Exception as e:
        print(e.args)