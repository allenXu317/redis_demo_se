import vote_cli as vc
import argparse


parser = argparse.ArgumentParser(description="redis_up_demo")
parser.add_argument("--name","-n",help="候选人的姓名")

args = parser.parse_args()
name = args.name
# 投赞成票：
vc.voteToUp(name)



