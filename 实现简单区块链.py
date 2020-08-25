import hashlib
import datetime

class  DaDaBlockCoin:#电子货币，达达币
    def __init__(self,index,#索引
               timestamp,#交易时间
               data,#交易记录
               pre_hash):#上一个哈希
        self.index = index
        self.timestamp=timestamp
        self.data=data
        self.prehash = pre_hash
        self.selfhash=self.hash_DaDaBlockCoin();#自身哈希
    def hash_DaDaBlockCoin(self):
        sha = hashlib.sha256() #加密算法
        datastr = str(self.index)+str(self.timestamp)+str(self.data)+str(self.prehash)#对于数据整体加密
        sha.update(datastr.encode('utf-8'))#二进制
        return sha.hexdigest()

def create_first_DaDaBlock():#创世区块链第一块
    return DaDaBlockCoin(0,datetime.datetime.now(),"Love DaDa",'123')

def create_money_DaDaBlock(last_block):#区块链的其他块
    this_index=last_block.index+1
    this_timestamp=datetime.datetime.now()
    this_data='love Dada'+str(this_index)
    this_prehash=last_block.selfhash#取得上一块的哈希
    return DaDaBlockCoin(this_index,this_timestamp,this_data,this_prehash)

DaDaBlockCoins=[create_first_DaDaBlock()]#区块链列表，只有一个创世模块
nums =5
head_block=DaDaBlockCoins[0]
print(head_block.index,head_block.timestamp,head_block.selfhash,head_block.prehash)
for i in range(nums):
    dadaBlock_add=create_money_DaDaBlock(head_block)#创建一个区块链的节点
    DaDaBlockCoins.append(dadaBlock_add) #加入区块
    head_block=dadaBlock_add
    print(dadaBlock_add.index,dadaBlock_add.timestamp,dadaBlock_add.selfhash,dadaBlock_add.prehash)
    
