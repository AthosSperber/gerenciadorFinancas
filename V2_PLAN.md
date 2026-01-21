# Plano de Execução V2 (dentro do mesmo repositório)

> **Nota**: O texto do *Repo Audit* não foi fornecido na solicitação. Este plano é um baseline seguro e minimalista para V2 com base no estado atual do repositório.

## Plano de commits (mínimo e seguro)

1. **Commit 1 — hygiene + documentação**
   - Adicionar este plano (V2_PLAN.md) e explicar o escopo V2.
   - Registrar premissas e decisões de stack.
2. **Commit 2 — tag legacy e isolamento do legado**
   - Criar tag `legacy-v1` apontando para o estado atual.
   - Mover o sistema atual para `/legacy` mantendo tudo *read-only* (sem refactors).
   - Atualizar `.gitignore`/docs para refletir a nova organização.
3. **Commit 3 — scaffold V2 mínimo**
   - Criar `/v2` com estrutura modular e CLI.
   - Adicionar schemas Pydantic e persistência append-only em SQLite.
4. **Commit 4 — ingestão + OCR + extração + persistência**
   - Implementar pipeline CLI: ingestão → OCR → extração → persistência → export.
5. **Commit 5 — testes mínimos e exemplos**
   - Adicionar testes de schemas e de persistência (smoke tests).
   - Documentar exemplos de uso no README de `/v2`.

## Estrutura de diretórios final

```
/legacy/                     # código V1 (read-only)
/v2/
  README.md
  pyproject.toml
  v2/
    __init__.py
    cli.py                   # Typer/argparse
    config.py                # env + paths
    ocr.py                   # wrapper pytesseract
    extract.py               # parsing/normalização
    models/
      __init__.py
      receipt.py             # Pydantic schemas
    store/
      __init__.py
      sqlite.py              # append-only
    export/
      __init__.py
      jsonl.py
    utils/
      hashing.py
      manifest.py
  data/
    raw/
    manifests/
    db.sqlite3
```

## Contratos de dados (Pydantic)

```python
from __future__ import annotations
from datetime import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field

class ReceiptRaw(BaseModel):
    receipt_id: str
    source_path: str
    captured_at: datetime
    sha256: str
    mime_type: str

class ReceiptExtracted(BaseModel):
    receipt_id: str
    ocr_text: str
    vendor_name: Optional[str] = None
    total: Optional[Decimal] = None
    currency: Optional[str] = None
    purchased_at: Optional[datetime] = None
    confidence: Optional[float] = None

class Transaction(BaseModel):
    transaction_id: str
    receipt_id: str
    amount: Decimal
    currency: str
    category: Optional[str] = None
    occurred_at: Optional[datetime] = None
    description: Optional[str] = None

class ArtifactMetadata(BaseModel):
    artifact_id: str
    receipt_id: str
    sha256: str
    byte_size: int
    created_at: datetime
    manifest_path: str
```

## Stack mínima (V2)

- **CLI**: Typer (ou argparse se preferir zero deps extra).
- **Schemas**: Pydantic.
- **OCR**: pytesseract, configurado por env (`TESSERACT_CMD`) sem hardcode de path.
- **Persistência**: SQLite append-only (MVP), com tabelas `receipt_raw`, `receipt_extracted`, `transactions`, `artifact_metadata`.
- **Export**: JSONL (inicial), com opção de CSV no backlog.

## Verificação e manifesto

- **Hash**: SHA-256 do artefato (arquivo de imagem/PDF).
- **Manifesto JSON**: salvo em `/v2/data/manifests/<receipt_id>.json` com:
  - `receipt_id`, `sha256`, `byte_size`, `source_path`, `captured_at`, `mime_type`.

## Fluxo CLI (MVP)

1. `v2 ingest <file>`
   - copia para `/v2/data/raw/`
   - calcula SHA-256
   - cria `ReceiptRaw` + `ArtifactMetadata`
   - grava manifesto JSON
2. `v2 ocr <receipt_id>`
   - aplica pytesseract
   - grava `ReceiptExtracted`
3. `v2 extract <receipt_id>`
   - heurísticas simples para `vendor_name`, `total`, `currency`, `purchased_at`
   - gera `Transaction` se possível
4. `v2 export --format jsonl --out <path>`
   - exporta append-only para consumo externo

## “Não fazer agora” (evitar escopo)

- Frontend web ou dashboards.
- Microserviços ou filas distribuídas.
- Modelos de ML próprios para extração.
- Integração com bancos/contas externas.
- Normalização avançada de categorias.
- Processamento em lote com orquestradores.

## Backlog curto (fases 2 e 3)

**Fase 2**
- Melhorar heurísticas de extração (regexs por país/idioma).
- Export CSV/Parquet.
- Validação cruzada de valores.

**Fase 3**
- UI mínima para revisão humana.
- Plug-in de storage remoto (S3/MinIO).
- Indexação full-text dos OCRs.
