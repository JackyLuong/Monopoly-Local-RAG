# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ["gui.py"],
    pathex=["."],
    binaries=[],
    datas=[("get_embeddings.py", "."), ("query_data.py", "."), ("chroma/chroma.sqlite3", "chroma")],
    hiddenimports=[
        "langchain.prompts", 
        "langchain_chroma", 
        "langchain_ollama", 
        "onnxruntime", 
        "chromadb", 
        "chromadb.api", 
        "chromadb.utils.embedding_functions",
        "chromadb.utils.embedding_functions.onnx_mini_lm_l6_v2",
        "pydantic.deprecated.decorator", 
        "query_data", 
        "chromadb.telemetry.product.posthog", 
        "chromadb.api.segment",
        "chromadb.db.impl",
        "chromadb.db.impl.sqlite",
        "chromadb.migrations",
        "chromadb.migrations.embeddings_queue",
        "chromadb.segment.impl.manager", 
        "chromadb.segment.impl.manager.local", 
        "chromadb.segment.impl.metadata", 
        "chromadb.segment.impl.metadata.sqlite", 
        "chromadb.segment.impl.vector", 
        "chromadb.segment.impl.vector.batch", 
        "chromadb.segment.impl.vector.brute_force_index", 
        "chromadb.segment.impl.vector.hnsw_params", 
        "chromadb.segment.impl.vector.local_hnsw", 
        "chromadb.segment.impl.vector.local_persistent_hnsw"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="gui",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
