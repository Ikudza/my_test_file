# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from lxml import etree
import codecs


def file_to_bd(filename):
    f = codecs.open(filename, "r")
    tree_file = etree.parse(f)

    nodes = tree_file.xpath('/message/sender')
    for node in nodes:
        print node.tag, node.text
        tag_name = node.xpath('name')
        for node_name in tag_name:
            print node_name.tag, node_name.text
        tag_inn = node.xpath('inn')
        for node_inn in tag_inn:
            print node_inn.tag, node_inn.text
    # tag: name - inn

    tag_area = tree_file.xpath('/message/area')
    for node in tag_area:
        print node.tag, node.keys(), node.values()
        tag_mpoint = node.xpath('measuringpoint')
        for node_mpoint in tag_mpoint:
            for i, elem in enumerate(node_mpoint.keys()):
                print elem, node_mpoint.values()[i]
            tag_mchannel = node_mpoint.xpath('measuringchannel')
            for node_mchannel in tag_mchannel:
                for i, elem in enumerate(node_mchannel.keys()):
                    print elem, node_mchannel.values()[i]
                tag_period = node_mchannel.xpath('period')
                for node_period in tag_period:
                    for i, elem in enumerate(node_period.keys()):
                        print elem, node_period.values()[i]
                    tag_value = node_period.xpath('value')
                    for node_value in tag_value:
                        for i, elem in enumerate(node_value.keys()):
                            print elem, node_value.values()[i]

    #  tag: name - inn  -
    #       measuringpoint-
    #           tag: measuringchannel(code,desc) -
    #               tag: period(start,end)-
    #                       tag:value(status)


if __name__ == '__main__':
    file_to_bd('test.xml')
