# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

##Import Django library
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

##Import note models
from .models import Note
from .forms import NoteForm

logger = logging.getLogger('django')

@login_required
def note(request):
    ''' note : view of the note page
            Templates: note.html
            Request_path: '/note'
            Context:
                note_id - note id
                notes - notes object
                note - note
    '''
    ##Get note form
    form = NoteForm()
    logger.info("Get note form.")

    ##Get all user notes
    user_note = Note.objects.filter(owner=request.user)
    logger.info("Get all user notes.")

    ##Get note id
    note_id = int(request.GET.get('note_id', 0))
    logger.info("Get now order id.")

    ##Context for template
    context = {
        'form': form,
        'note_id': note_id,
        'user_note': user_note,
    }

    ##If user save note, get note id and content to create a new note
    if request.method == 'POST':
        logger.info("Request method is POST, get note info and save.")

        note_id = int(request.POST.get('note_id', 0))
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        note = Note.objects.create(title=title, content=content, owner=request.user)
        logger.info("note_id: %d" % (note_id))
        logger.info("title: %s" % (title))
        logger.info("content: %s" % (content))
        logger.info("note: %s" % (note))

        return redirect('/note')

    logger.info("Request method is GET, return note page.")
    return render(request, 'note.html', context)

@login_required
def delete_note(request, note_id):
    ''' delete_note : view of delete note
            Templates: N/A
            Request_path: '/delete_note/{{note_id}}'
            Context: N/A
    '''
    ##Get note with note id
    try:
        logger.info("Get note by note id: %s" % (note_id))
        note = Note.objects.get(pk=note_id)
    except:
        logger.info("Don't have this note id: %s" % (note_id))
        return redirect('/note')

    ##Check the note owned by login user and delete
    if note.owner == request.user:
        logger.info("Delete note id: %s" % (note_id))
        note.delete()
    else:
        logger.warning("Delete note id: %s fail, not note owner." % (note_id))

    return redirect('/note')