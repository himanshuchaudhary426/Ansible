#!/bin/python

import sys
try:
    import boto3
except Exception as e:
    print(e)
    print("Please rectify the exception and try again")
    sys.exit(1)
def get_hosts(ec2_ob, fv):
    f = {"Name":"tag:Env", "Values":[fv]}
    for each_in in ec2_ob.instances.filter(Filters=[f]):
        print(each_in.private_ip_address)
    return none
def main():
    ec2_ob = boto3.resource("ec2","us-east-1")
    db_group = get_hosts(ec2_ob, 'db')
    app_group = get_hosts(ec2_ob, 'app')

if __name__=="__main__":
    main()
