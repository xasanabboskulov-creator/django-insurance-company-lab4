from django.shortcuts import render
from django.http import Http404
from .models import Contract


def archive(request):
    contracts = Contract.objects.select_related(
        'client',
        'agent',
        'branch',
        'insurance_type'
    ).all()

    return render(request, 'archive.html', {
        'contracts': contracts
    })


def get_contract(request, contract_id):
    try:
        contract = Contract.objects.select_related(
            'client',
            'agent',
            'branch',
            'insurance_type'
        ).get(id=contract_id)

        return render(request, 'article.html', {
            'post': contract
        })

    except Contract.DoesNotExist:
        raise Http404