def greeting(type,occasion ,name ="none", time = "general"):
    formal = {"Job Interview":f"Good {time} , Mr.{name} i am {user['n1']}. i am here for the interview",
              "Formal Invitations" : "hello dear , {user['n1']} here i wanted u to join us on the occasion of {occasion}",
                "Business Meeting": f"Good {time} everyone , i am here for presenting ",
                "Networking Event":f"Good evening. It's a pleasure to be here and connect with such a diverse group of professionals./n I'm {user["n1"]}, and I'm looking forward to some insightful conversations today.",
                "Academic Ceremony":f"Respected dignitaries, honored faculty members, and dear fellow students, good {time}.\n  It is a great privilege to be present here today for this {occasion} that celebrates learning, dedication, and achievement.",
                "Diplomatic Function":f"Respected ambassadors, honored guests, and distinguished colleagues, good {time}.\n I am delighted to join you at this important occasion that celebrates dialogue, partnership, and mutual understanding.",
                "Legal Proceedings":f"Respected ambassadors, honored guests, and distinguished colleagues, good {time}."/
                  f" I am {user["n1"]} delighted to join you at this important occasion that celebrates dialogue, partnership, and mutual understanding."}
    informal_but_respectful = {"adressing one":"hello Mr.{name} , how are you","adressing many":"hey everyone , hows everyone doing","leaving":"byy! it was a nice time with you"}
    casual = {"adressing friends":f"hello Mr.{name} , how are you","adressing peps in acthe hood":"heyy mann!! hows it going ? "}
                
    