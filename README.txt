Aamarpay Payment Gateway integration in python
======


aamarpay is an online payment gateway service for Bangladesh. Committed to provide best payment experience online for business. Lowest fee and fast checkout will give you good experience of receiving payment online.


Installation
~~~~~~~~~~~~

We recommend install ``aamarpay`` through pip install .

.. code:: bash

    $ pip install aamarpay

Example
~~~~~~~
	
To make a payment :

.. code:: python

    from aamarpay.aamarpay import aamarPay
    pay = aamarPay(isSandbox=True,transactionAmount=600)
    paymentpath = pay.payment()
    return redirect(paymentpath)
    # Output: paymentpath output https://sandbox.aamarpay.com/paynow.php?track=AAM1636017211119390#
	
Contribute
~~~~~~~~~~

Create Github Pull Request https://github.com/sanjidbillah/aamarPay-python

x
Thanks
~~~~~~

