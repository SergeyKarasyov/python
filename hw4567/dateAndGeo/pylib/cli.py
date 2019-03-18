#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
from date_module import str2datetime
from geo_module import string2geo


@click.group()
def cli():
    pass


@cli.command('str2date')
@click.argument('datestring')
def conver2date(datestring):
    click.echo("str2date {}".format(datestring))
    print(str2datetime(datestring))


@cli.command('str2geo')
@click.argument('geostring')
def conver2geo(geostring):
    click.echo("str2geo {}".format(geostring))
    print(string2geo(geostring))


if __name__ == "__main__":
    cli()
