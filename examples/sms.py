from context import jc, mobile, image
import sys
import datetime

def send_code():
    return jc.send_code(mobile, '1')

def send_voice_code():
    return jc.send_voice_code(mobile)

def verify_code(msg_id, code):
    return jc.verify_code(msg_id, code)

def create_tmpl_task():
    time = (datetime.datetime.now() + datetime.timedelta(days=60)).strftime("%Y-%m-%d %H:%M:%S")
    return jc.send_teml(mobile, 1, { 'code': 'jiguang' }, time)

def show_tmpl_task(schedule_id):
    return jc.show_schedule_message(schedule_id)

def delete_tmpl_task(schedule_id):
    return jc.delete_schedule_message(schedule_id)


def text_code():
    response = send_code()
    print(response)
    msg_id = response['msg_id']
    code = input('code you received on the phone: ')
    response = verify_code(msg_id, code)
    print(response)

def voice_code():
    response = send_voice_code()
    print(response)
    msg_id = response['msg_id']
    code = input('voice code you received on the phone: ')
    response = verify_code(msg_id, code)
    print(response)

def tmpl_task():
    response = create_tmpl_task()
    print('create template message:')
    print(response)
    schedule_id = response['schedule_id']
    response = show_tmpl_task(schedule_id)
    print('show template message:')
    print(response)
    response = delete_tmpl_task(schedule_id)
    print('delete template message:')
    print(response)

def blance():
    response = jc.app_balance()
    print(response)

# def create_sign():
#     with open(image, 'rb') as im:
#         response = jc.create_sign('test', im, remark='ssss')
#         print(response)

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        eval(sys.argv[1])()
    elif (len(sys.argv) == 3):
        eval(sys.argv[1])(sys.argv[2])
    else:
        print('Oops')
