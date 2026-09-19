import hashlib
import pathlib
import types


class UserError(Exception):
    pass


class Address(str):
    pass


class TreeMap(dict):
    @classmethod
    def __class_getitem__(cls, _item):
        return cls


class DynArray(list):
    @classmethod
    def __class_getitem__(cls, _item):
        return cls


class Keccak256:
    def __init__(self):
        self.value = hashlib.sha3_256()

    def update(self, data):
        self.value.update(data)

    def hexdigest(self):
        return self.value.hexdigest()


class Event:
    def emit(self):
        pass


class Public:
    write = staticmethod(lambda fn: fn)
    view = staticmethod(lambda fn: fn)


class Nondet:
    responses = []

    @classmethod
    def exec_prompt(cls, _prompt, **_kwargs):
        return cls.responses.pop(0)


class EqPrinciple:
    @staticmethod
    def prompt_comparative(fn, *_args, **_kwargs):
        return fn()


gl = types.SimpleNamespace(
    Contract=object,
    Event=Event,
    public=Public(),
    vm=types.SimpleNamespace(UserError=UserError),
    message=types.SimpleNamespace(sender_address=Address("0xaaa")),
    nondet=Nondet,
    eq_principle=EqPrinciple(),
)
namespace = {
    "Address": Address,
    "TreeMap": TreeMap,
    "DynArray": DynArray,
    "Keccak256": Keccak256,
    "allow_storage": lambda cls: cls,
    "u32": int,
    "gl": gl,
}
root = pathlib.Path(__file__).resolve().parents[1]
source = (root / "contract.py").read_text().replace("from genlayer import *", "")
exec(compile(source, str(root / "contract.py"), "exec"), namespace)


def fresh():
    clusterer = namespace["Cluster"]()
    clusterer.clusterings = TreeMap()
    clusterer.open_clustering("case", "same real-world record")
    clusterer.submit_records("case", ["A", "A alias", "B"])
    return clusterer


def run(bits):
    clusterer = fresh()
    Nondet.responses = ["{\"same\":" + str(bits).replace(" ", "") + "}"]
    clusterer.cluster("case")
    return clusterer


def duplicates():
    clusterer = run([1, 0, 0])
    assert clusterer.get_labels("case") == [0, 0, 1]


def all_distinct():
    clusterer = run([0, 0, 0])
    assert clusterer.get_labels("case") == [0, 1, 2]


def transitive_tension():
    clusterer = run([1, 0, 1])
    assert clusterer.get_labels("case") == [0, 0, 0]
    assert clusterer.clusterings["case"].tension_pairs == ["0-2"]


def duplicate_guard():
    clusterer = namespace["Cluster"]()
    clusterer.clusterings = TreeMap()
    clusterer.open_clustering("case", "same")
    try:
        clusterer.submit_records("case", ["A", "a"])
    except UserError as exc:
        assert str(exc) == "DUPLICATE_RECORD"
        return
    raise AssertionError("DUPLICATE_RECORD")


tests = [duplicates, all_distinct, transitive_tension, duplicate_guard]
for test in tests:
    test()
    print("PASS", test.__name__)
print(f"{len(tests)}/{len(tests)} pass")
