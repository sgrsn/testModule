from setuptools import setup, find_packages

__author__ = 'Hidaka Sato'


setup(
    name='TSET',  # ライブラリの名前
    version='1.0',  # バージョン
    description='モジュール配布のテスト',  # 解説
    author='Hidaka Sato',  # 作った人
    author_email='sato@suzakugiken.jp',  # 作った人の連絡先
    url='https://github.com/sgrsn/testModule',  # URL(Githubリポジトリ)
    classifiers=[  # 注記事項(開発ステータス,利用目的,LICENSEなど)
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=find_packages(),  # 梱包するコードの場所. setuptoolsのfind_packages()でパッケージなdirectoryを捜索&よしなに突っ込んでくれます
    include_package_data=True,  # ソースコード(*.py)以外のファイルも入れるか否か
    keywords=['baseball', 'MLB', 'MLBAM'],  # キーワード
    license='MIT License',  # ライセンス
    install_requires=[  # 依存ライブラリ
    ],
    entry_points="""  # コマンドラインにするときのエントリーポイント、pitchpx/__init__.pyの関数をエントリーポイントにしました.
        [console_scripts]
        pitchpx = pitchpx:main
    """,
)