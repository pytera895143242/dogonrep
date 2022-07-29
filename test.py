session = [0]

for i in range(1,5):
    last_session = session[-1]
    print('Последняя сессия:', last_session)
    session.append(last_session + 1 )

print(session)