import pytest
import os
from main import dicionarioComentario

@pytest.fixture

def testGetComentariosYaml(dicionarioComentario):
    # Teste para verificar se a função testGetComentariosYaml retorna uma lista de comentários não vazia
    assert len(dicionarioComentario) > 0

def testYamlFileCreated():
    # Teste para verificar se o arquivo "Comentarios.yaml" foi criado
    assert os.path.exists("Comentarios.yaml")