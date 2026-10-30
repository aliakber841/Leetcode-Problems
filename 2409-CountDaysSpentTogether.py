def dayOfYear(month,day):
    month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    total=0
    for m in range(month-1):
        total+=month_days[m]
    total+=day
    return total

class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        alice_arrive_month=int(arriveAlice[0:2])
        bob_arrive_month=int(arriveBob[0:2])
        alice_arrive_day=int(arriveAlice[3:])
        bob_arrive_day=int(arriveBob[3:])

        alice_leave_month=int(leaveAlice[0:2])
        bob_leave_month=int(leaveBob[0:2])
        alice_leave_day=int(leaveAlice[3:])
        bob_leave_day=int(leaveBob[3:])

        alice_arrive=dayOfYear(alice_arrive_month,alice_arrive_day)
        alice_leave=dayOfYear(alice_leave_month,alice_leave_day)
        bob_arrive=dayOfYear(bob_arrive_month,bob_arrive_day)
        bob_leave=dayOfYear(bob_leave_month,bob_leave_day)

        start=max(alice_arrive,bob_arrive)
        end=min(alice_leave,bob_leave)

        if end<start:
            return 0
        return end-start+1