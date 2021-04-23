from Enrollment.services import unit_of_work


def members_view(first_name: str, uow: unit_of_work.SqlAlchemyUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT first_name, last_name, age,gender,active FROM members WHERE first_name = :first_name
            """,
            dict(first_name=first_name),
        )
    return [dict(r) for r in results]