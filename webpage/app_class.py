from .models import SessionDB


class Session():
    def __init__(self, SessionDB):
        self.token = SessionDB.token
        self.problem_num = int(SessionDB.problem_num)
        self.life = int(SessionDB.life)
        self.description = SessionDB.description
        self.option = [SessionDB.option1, SessionDB.option2, SessionDB.option3, SessionDB.option4]
        self.result = [int(SessionDB.result1), int(SessionDB.result2), int(SessionDB.result3), int(SessionDB.result4)]
        self.result_text = SessionDB.result_text
        self.conv_archive = SessionDB.conv_archive
        self.image_num = SessionDB.image_num

    @staticmethod
    def create(token, problem_num, life, description, option, result, result_text, conv_archive, image_num):
        return Session(
            token = token,
            problem_num = problem_num,
            life = life,
            description = description,
            option = [option[0], option[1], option[2], option[3]],
            result = [result[0], result[1], result[2], result[3]],
            result_text = result_text,
            conv_archive = conv_archive,
            image_num = image_num
        )

    def update(self, SessionDB):
        self.token = SessionDB.token
        self.problem_num = int(SessionDB.problem_num)
        self.life = int(SessionDB.life)
        self.description = SessionDB.description
        self.option = [SessionDB.option1, SessionDB.option2, SessionDB.option3, SessionDB.option4]
        self.result = [int(SessionDB.result1), int(SessionDB.result2), int(SessionDB.result3), int(SessionDB.result4)]
        self.result_text = SessionDB.result_text
        self.conv_archive = SessionDB.conv_archive
        self.image_num = SessionDB.image_num
    
    def to_session_db(self):
        return SessionDB(
            token=self.token,
            problem_num=self.problem_num,
            life=self.life,
            description=self.description,
            option1=self.option[0],
            option2=self.option[1],
            option3=self.option[2],
            option4=self.option[3],
            result1=self.result[0],
            result2=self.result[1],
            result3=self.result[2],
            result4=self.result[3],
            result_text=self.result_text,
            conv_archive = self.conv_archive,
            image_num=self.image_num
        )
    

class Problem(Session):
    def __init__(self, session: Session):
        super().__init__(session.to_session_db())

class Check(Session):
    def __init__(self, session: Session, select_number: int):
        super().__init__(session.to_session_db())
        self.select_number = select_number


class Start(Session):
    def __init__(self, session: Session):
        super().__init__(session.to_session_db())

class Gameover(Session):
    def __init__(self, session: Session):
        super().__init__(session.to_session_db())