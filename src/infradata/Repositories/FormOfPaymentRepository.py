from src.application.DTOs.FormOfPaymentDTO import FormOfPaymentDTO
from src.application.Services.ResponseWrapper import ResponseWrapper
from src.domain.repositories.IFormOfPaymentRepository import IFormOfPaymentRepository
from src.infradata.Context.ApplicationDbContext import ApplicationDbContext
from src.infradata.Maps.FormOfPaymentMap import FormOfPaymentMap
from sqlalchemy.exc import SQLAlchemyError


class FormOfPaymentRepository(IFormOfPaymentRepository):

    @classmethod
    def get_movie_Id_info(cls, movie_id: str) -> ResponseWrapper:
        with ApplicationDbContext() as database:
            try:
                database.session.begin()
                list_form_of_payment = (
                    database.session
                    .query(FormOfPaymentMap.FormName, FormOfPaymentMap.Price)
                    .filter(FormOfPaymentMap.MovieId == movie_id)
                    .all()
                )
                database.session.commit()

                if list_form_of_payment != None:
                    array = []
                    for el in list_form_of_payment:
                        form_of_payment_dto = FormOfPaymentDTO(
                            id=None, formName=el.FormName, price=el.Price, movieId=None).to_dict()
                        array.append(form_of_payment_dto)

                    return ResponseWrapper.ok(array)
                else:
                    return ResponseWrapper.ok(list_form_of_payment)
            except SQLAlchemyError as exception:
                database.session.rollback()
                exception_name = type(exception).__name__
                return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")

    @classmethod
    def create(cls, form_of_payment_map: FormOfPaymentMap) -> ResponseWrapper:
        with ApplicationDbContext() as database:

            form_of_payment_dto = FormOfPaymentDTO(
                id=None, formName=form_of_payment_map.FormName, price=form_of_payment_map.Price, movieId=None).to_dict()

        try:
            database.session.begin()
            database.session.add(form_of_payment_map)
            database.session.commit()
            return ResponseWrapper.ok(form_of_payment_dto)
        except SQLAlchemyError as exception:
            database.session.rollback()
            exception_name = type(exception).__name__
            return ResponseWrapper.fail(f"Erro: {exception_name}, Detalhes: {str(exception)}")
