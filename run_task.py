import time
from vantage6.client import Client

# User authentication
client = Client("http://localhost", 5000, "/api")
client.authenticate("leia", "12345")
client.setup_encryption(None)

# Input for task
input_ = {
    "master": "true",
    "method":"master", 
    "args": [
        {
            "PatientID":"category",
            "age":"float64",
            "gender": "category",
            "Clinical.T.Stage":"category",
            "Clinical.N.Stage":"category",
            "Survival.time": "Int64",
            "deadstatus.event": "Int64"
        },
        ".", # decimal indicator
        "," # csv delimiter
    ],
    "kwargs": {}
}

# Run summary algorithm task
task = client.post_task(
    name="testing",
    image="harbor.vantage6.ai/algorithms/summary",
    collaboration_id=1,
    input_= input_,
    organization_ids=[2, 3]
)

# Keep performing GET requests until results are ready (max 50 attempts)
print("Wait and fetch results")
res = client.result.get(id_=task.get("results")[0]['id'])
attempts = 1
while((res["finished_at"] == None) and attempts < 50):
    print("waiting...")
    time.sleep(5)
    res = client.result.get(id_=task.get("results")[0]['id'])
    attempts += 1

print('Task result:')
print(res['result'])
