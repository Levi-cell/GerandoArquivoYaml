"""Fazendo testes"""
import os
import pytest


@pytest.fixture

def test_get_comentarios_yaml(dicionario_comentario):
    """Verificano se ele tem caracters"""
    assert len(dicionario_comentario) > 0

def test_yaml_file_created():
    """Testando se o arquivo existe"""
    assert os.path.exists("Comentarios.yaml")
