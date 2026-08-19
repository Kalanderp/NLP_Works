"""Rule-based dialog-act recognition."""
def act(utterance):
 u=utterance.lower().strip()
 if u.endswith('?') or u.startswith(('who','what','when','where','why','how','can','could','do')): return 'QUESTION'
 if u.startswith(('please','could you','would you')): return 'REQUEST'
 if any(x in u for x in ('thank','thanks')): return 'THANK'
 if any(x in u for x in ('hello','hi','good morning')): return 'GREETING'
 if any(x in u for x in ('bye','goodbye')): return 'GOODBYE'
 return 'STATEMENT'
if __name__=='__main__':
 for u in ['Hello there!','Could you open the door?','Thanks for your help.','The meeting starts at ten.']: print(u,'->',act(u))
