from xml.etree import ElementTree as ET

L = "{http://www.lido-schema.org}"


def from_file(filepath):
    return to_dict(ET.parse(filepath))


def from_string(lidodoc):
    return to_dict(ET.fromstring(lidodoc))


def to_dict(lidonode):
    fields = {}
    for field, xpath_string in [
        (
            "recordInfoLink",
            f".//{L}administrativeMetadata/{L}recordWrap/{L}recordInfoSet/{L}recordInfoLink",
        ),
        (
            "image",
            f".//{L}administrativeMetadata/{L}resourceWrap/{L}resourceSet/{L}resourceRepresentation/{L}linkResource",
        ),
        (
            "description",
            f".//{L}administrativeMetadata/{L}resourceWrap/{L}resourceSet/{L}resourceDescription",
        ),
        (
            "objectWorkType",
            f".//{L}descriptiveMetadata/{L}objectClassificationWrap/{L}objectWorkTypeWrap/{L}objectWorkType/{L}conceptID",
        ),
        (
            "classification",
            f".//{L}descriptiveMetadata/{L}objectClassificationWrap/{L}classificationWrap/{L}classification/{L}conceptID",
        ),
        (
            "title",
            f".//{L}descriptiveMetadata/{L}objectIdentificationWrap/{L}titleWrap/{L}titleSet/{L}appellationValue",
        ),
        (
            "legalBody",
            f".//{L}descriptiveMetadata/{L}objectIdentificationWrap/{L}repositoryWrap/{L}repositorySet/{L}repositoryName/{L}legalBodyID",
        ),
        (
            "location",
            f".//{L}descriptiveMetadata/{L}objectIdentificationWrap/{L}repositoryWrap/{L}repositorySet/{L}repositoryLocation/{L}placeID",
        ),
        (
            "subjects",
            f".//{L}descriptiveMetadata/{L}objectRelationWrap/{L}subjectWrap/{L}subjectSet/{L}subject/{L}subjectConcept/{L}conceptID",
        ),
        (
            "related",
            f".//{L}descriptiveMetadata/{L}objectRelationWrap/{L}relatedWorksWrap/{L}relatedWorkSet/{L}relatedWork/{L}object/{L}objectID",
        ),
        (
            "relatedNote",
            f".//{L}descriptiveMetadata/{L}objectRelationWrap/{L}relatedWorksWrap/{L}relatedWorkSet/{L}relatedWork/{L}object/{L}objectNote",
        ),
        (
            "actor",
            f"{L}descriptiveMetadata/{L}eventWrap/{L}eventSet/{L}event/{L}eventActor/{L}actorInRole/{L}actor/{L}actorID",
        ),
        (
            "materials",
            f"{L}descriptiveMetadata/{L}eventWrap/{L}eventSet/{L}event/{L}eventMaterialsTech/{L}materialsTech/{L}termMaterialsTech/{L}conceptID",
        ),
        (
            "displayDate",
            f"{L}descriptiveMetadata/{L}eventWrap/{L}eventSet/{L}event/{L}eventDate/{L}displayDate",
        ),
        (
            "earliestDate",
            f"{L}descriptiveMetadata/{L}eventWrap/{L}eventSet/{L}event/{L}eventDate/{L}date/{L}earliestDate",
        ),
        (
            "latestDate",
            f"{L}descriptiveMetadata/{L}eventWrap/{L}eventSet/{L}event/{L}eventDate/{L}date/{L}latestDate",
        ),
        (
            "displayDate",
            f".//{L}descriptiveMetadata/{L}objectRelationWrap/{L}subjectWrap/{L}subjectSet/{L}subject/{L}subjectEvent/{L}event/{L}eventDate/{L}displayDate",
        ),
        (
            "earliestDate",
            f".//{L}descriptiveMetadata/{L}objectRelationWrap/{L}subjectWrap/{L}subjectSet/{L}subject/{L}subjectEvent/{L}event/{L}eventDate/{L}date/{L}earliestDate",
        ),
        (
            "latestDate",
            f".//{L}descriptiveMetadata/{L}objectRelationWrap/{L}subjectWrap/{L}subjectSet/{L}subject/{L}subjectEvent/{L}event/{L}eventDate/{L}date/{L}latestDate",
        ),
        (
            "place",
            f".//{L}descriptiveMetadata/{L}objectRelationWrap/{L}subjectWrap/{L}subjectSet/{L}subject/{L}subjectEvent/{L}event/{L}eventPlace/{L}displayPlace",
        ),
        (
            "actor",
            f".//{L}descriptiveMetadata/{L}objectRelationWrap/{L}subjectWrap/{L}subjectSet/{L}subject/{L}subjectEvent/{L}event/{L}eventActor/{L}displayActor",
        ),
        (
            "description",
            f".//{L}descriptiveMetadata/{L}objectIdentificationWrap/{L}objectDescriptionWrap/{L}objectDescriptionSet/{L}descriptiveNoteValue",
        ),
        ("recordID", f".//{L}administrativeMetadata/{L}recordWrap/{L}recordID"),
    ]:
        fields.setdefault(field, []).extend(
            [n for n in lidonode.findall(xpath_string) if n.text]
        )
    return dict([(f, ff) for f, ff in fields.items() if len(ff) > 0])
