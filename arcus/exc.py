from typing import Optional, Union

from requests import HTTPError


class ArcusException(Exception):
    """Generic Arcus API exception"""


class InvalidAuth(ArcusException):
    """Invalid API authentication credentials"""


class InvalidBiller(ArcusException):
    def __init__(self, biller_id: Union[int, str]):
        self.message = f'{biller_id} is an invalid biller_id'


class NotFound(ArcusException, HTTPError):
    pass


class UnprocessableEntity(ArcusException):
    def __init__(self, code: str, message: Optional[str] = None, **kwargs):
        self.code = code
        if message:
            self.message = message
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def __repr__(self):
        return (
            self.__class__.__name__
            + '('
            + ', '.join(
                [
                    f'{attr}={repr(value)}'
                    for attr, value in self.__dict__.items()
                ]
            )
            + ')'
        )

    def __str__(self):
        return getattr(self, 'message', self.__class__.__doc__)


class InvalidAccountNumber(UnprocessableEntity):
    def __init__(self, code: str, account_number: str, biller_id: int,
                 **kwargs):
        message = (
            f'{account_number} is an invalid account_number for biller '
            f'{biller_id}'
        )
        super().__init__(
            code, message, biller_id=biller_id, account_number=account_number,
            **kwargs
        )


class InvalidOperation(UnprocessableEntity):
    def __init__(self, code: str, transaction_id: Union[int, str], **kwargs):
        message = f'Unable to cancel the transaction {transaction_id}'
        super().__init__(code, message=message, transaction_id=transaction_id,
                         **kwargs)


class InvalidAmount(UnprocessableEntity):
    def __init__(self, code: str, amount: float, **kwargs):
        message = f'Invalid amount: {amount}'
        super().__init__(code, message=message, **kwargs)


class AlreadyPaid(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Payment already made'
        super().__init__(code, message=message, **kwargs)


class RecurrentPayments(UnprocessableEntity):
    def __init__(self, code: str,  **kwargs):
        message = f'Recurrent payments enabled'
        super().__init__(code, message=message, **kwargs)


class DuplicatedPayment(UnprocessableEntity):
    def __init__(self, code: str, amount: float, **kwargs):
        message = f'Duplicated payment for {amount}'
        super().__init__(code, message, amount=amount, **kwargs)


class IncompleteAmount(UnprocessableEntity):
    def __init__(self, code: str, amount: float, **kwargs):
        message = (
            f'Incomplete payment amount of {amount}, must pay full balance'
        )
        super().__init__(code, message, amount=amount, **kwargs)


class Forbidden(ArcusException):
    """Method Not Allowed"""


class UnexpectedError(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Unexpected error. Failed to make the consult'
        super().__init__(code, message=message, **kwargs)


class InvalidOrMissingParameters(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Invalid or missing parameters'
        super().__init__(code, message=message, **kwargs)


class InvalidBalance(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Account Balance is 0 or not enough'
        super().__init__(code, message=message, **kwargs)


class FailedConsult(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Failed to make the consult, please try again later'
        super().__init__(code, message=message, **kwargs)


class LimitExceeded(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Limit of transactions exceeded'
        super().__init__(code, message=message, **kwargs)


class BillerMaintenance(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Biller maintenance in progress, please try again later'
        super().__init__(code, message=message, **kwargs)


class ReversalNotSupported(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Reversal not supported'
        super().__init__(code, message=message, **kwargs)


class BillerConnection(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Timeout from biller'
        super().__init__(code, message=message, **kwargs)


class CancellationError(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Error with performing the cancellation'
        super().__init__(code, message=message, **kwargs)


class OverdueBill(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Overdue Bill'
        super().__init__(code, message=message, **kwargs)


class InvalidPhone(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Invalid Phone Number'
        super().__init__(code, message=message, **kwargs)


class FraudSuspected(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Fraud suspected'
        super().__init__(code, message=message, **kwargs)


class InvalidCurrency(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Invalid Currency'
        super().__init__(code, message=message, **kwargs)


class InvalidCompany(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Invalid company'
        super().__init__(code, message=message, **kwargs)


class InvalidBarCode(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Invalid Barcode Format.'
        super().__init__(code, message=message, **kwargs)


class InvalidCustomerStatus(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Invalid Customer Status.'
        super().__init__(code, message=message, **kwargs)


class DailyPaymentsLimit(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'The maximum number of payments on this day was reached'
        super().__init__(code, message=message, **kwargs)


class BalanceNotFound(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Can\'t get balance.'
        super().__init__(code, message=message, **kwargs)


class InvalidSubscription(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Invalid Subscription ID. Verify the ID or create a new'
        super().__init__(code, message=message, **kwargs)


class InvalidPOS(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'POS number is invalid'
        super().__init__(code, message=message, **kwargs)


class AccessDenied(UnprocessableEntity):
    def __init__(self, code: str, **kwargs):
        message = f'Processor Access Denied'
        super().__init__(code, message=message, **kwargs)


ARCUS_EXCEPTIONS = dict(
    R1=InvalidAccountNumber,
    R2=InvalidAccountNumber,
    R3=IncompleteAmount,
    R4=InvalidAccountNumber,
    R5=InvalidAccountNumber,
    R6=InvalidBiller,
    R7=RecurrentPayments,
    R8=AlreadyPaid,
    R9=UnexpectedError,
    R10=InvalidAccountNumber,
    R11=IncompleteAmount,
    R12=AlreadyPaid,
    R13=InvalidOrMissingParameters,
    R14=InvalidAmount,
    R15=InvalidBalance,
    R16=FailedConsult,
    R17=InvalidAmount,
    R18=LimitExceeded,
    R19=InvalidBiller,
    R20=InvalidBiller,
    R21=InvalidBiller,
    R22=BillerMaintenance,
    R23=ReversalNotSupported,
    R24=BillerConnection,
    R25=CancellationError,
    R26=ReversalNotSupported,
    R27=OverdueBill,
    R28=InvalidAccountNumber,
    R29=InvalidAccountNumber,
    R30=InvalidCompany,
    R31=InvalidPhone,
    R32=InvalidAmount,
    R33=FraudSuspected,
    R34=InvalidCurrency,
    R35=FailedConsult,
    R36=DuplicatedPayment,
    R37=RecurrentPayments,
    R41=IncompleteAmount,
    R42=InvalidBalance,
    R43=InvalidBarCode,
    R44=InvalidCustomerStatus,
    R45=DailyPaymentsLimit,
    R46=BalanceNotFound,
    R47=BillerConnection,
    R48=BillerConnection,
    R99=UnexpectedError,
    R100=InvalidBalance,
    R101=BalanceNotFound,
    R102=InvalidAmount,
    R103=ReversalNotSupported,
    R104=InvalidSubscription,
    R105=ReversalNotSupported,
    R114=InvalidAmount,
    R115=InvalidPOS,
    R117=InvalidCompany,
    R121=BalanceNotFound,
    R122=BalanceNotFound,
    R201=AccessDenied,
    R202=BalanceNotFound,
    R299=UnexpectedError,
)


def raise_arcus_exception(
        ex: UnprocessableEntity,
        account_number: str,
        biller_id: int,
        amount: Optional[float] = 0):
    exc = ARCUS_EXCEPTIONS[ex.code]
    raise exc(
        ex.code,
        account_number=account_number,
        biller_id=biller_id,
        amount=amount)
