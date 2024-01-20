# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'fct_ies.alumno'
    _description = 'Modelo de alumno'
    
    name = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")

    curso_academico = fields.Char(string="Curso académico", required=True)

    correo_electronico = fields.Char(string="Correo electrónico")
    telefono = fields.Char(string="Teléfono")
    ciclo_formativo = fields.Selection([('DAM', 'DAM'), ('DAW', 'DAW'), ('ASIR', 'ASIR')], string="Ciclo formativo", required=True)
    periodo_practica = fields.Selection([('abril', 'Abril'), ('septiembre', 'Septiembre')], string="Periodo de práctica", required=True)
    nota_media = fields.Float(string="Nota media", required=True)
    nota_media_texto = fields.Char(string="Nota media en texto", compute="_compute_nota_media_texto", store=True)
    
    empresa = fields.Many2one('fct_ies.empresa', string="Empresa")
    
    @api.depends('nota_media')
    def _compute_nota_media_texto(self):
        for record in self:
            if record.nota_media < 5:
                record.nota_media_texto = "Suspenso"
            elif record.nota_media < 7:
                record.nota_media_texto = "Aprobado"
            elif record.nota_media < 9:
                record.nota_media_texto = "Notable"
            elif record.nota_media < 10:
                record.nota_media_texto = "Sobresaliente"



class Empresa(models.Model):
    _name = 'fct_ies.empresa'
    _description = 'Modelo de empresa'

    name = fields.Char(string="Nombre", required=True)
    persona_contacto = fields.Char(string="Persona de contacto", required=True)
    telefono_contacto = fields.Char(string="Teléfono de contacto", required=True)
    correo_electronico = fields.Char(string="Correo electrónico", required=True)
    direccion = fields.Char(string="Dirección", required=True)
    
    alumnos = fields.One2many('fct_ies.alumno', 'empresa', string="Alumnos")