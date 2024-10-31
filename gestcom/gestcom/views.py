
from django.http import JsonResponse


def get_access_token(request):
    custumer_key = "x0KE0iJkwBORfq1L5VyaWFCTwaLDh8nv81AGSxJ9pyGsHmfk"
    customer_secret = "aB5dkW9uGL6xPQ57WZRw4TVKCCvwCMqdnROEvG1W7WUJfhuATGc7S3ALthC14IyF"
    access_toten_url ="https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    
    header = {'Content_type': 'application/json'}
    auth =(custumer_key,customer_secret)
    
    try:
        response = requests.get(access_toten_url,headers=header,auth=auth)
        response.raise_for_status()
        result =response.json()
        access_token = result['access_token']
        return JsonResponse({'access_token': access_token})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)})
    
    