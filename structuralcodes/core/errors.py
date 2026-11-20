"""General exception and warning classes."""


class StructuralCodesWarning(Warning):
    """Base class for StructurlCodes warnings."""


class NoConvergenceWarning(StructuralCodesWarning):
    """Warning for lack of convergence.

    A warning tht The solution should be inspected with care.
    """


class InformationWarning(StructuralCodesWarning):
    """Warning for simple information.
    xxx
    A warning that indicatekj is not invalid.
    """
