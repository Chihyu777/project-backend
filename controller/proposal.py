from flask import Blueprint, request, Response
from model import proposalModel
import json
from coder import MyEncoder
from .util import (ret, checkParm)


proposalAPI = Blueprint("proposal", __name__, url_prefix="/proposal")


@proposalAPI.route("/", methods=["GET"])
def find():
    cond = ["id", "term",  "ststusid", ]
    return ret(proposalModel.list({}))


@proposalAPI.route("/msg", methods=["POST"])
def msg():
    content = request.json
    cond = ["user_id", "content", "article_id", "parent_id"]
    t = checkParm(cond, content)
    if(t == ""):
        data = proposalModel.msg(
            account=content[cond[0]], mes=content[cond[1]], article_id=content[cond[2]], parent_id=content[cond[3]])
    else:
        data = {"success": False, "mes": t}
    print(data)
    return ret(data)


@proposalAPI.route("/msg/<p_id>", methods=["GET"])
def search(p_id):
    return ret(proposalModel.msgList(p_id))


@proposalAPI.route("/vote", methods=["POST"])
def vote():
    content = request.json
    cond = ["user_id", "sp_id", "proposal_id"]
    t = checkParm(cond, content)
    if(t == ""):
        data = proposalModel.vote(
            userid=content[cond[0]], sp_id=content[cond[1]], proposal_id=content[cond[2]])
    else:
        data = {"success": False, "mes": t}
    print(data)
    return ret(data)


@proposalAPI.route("/save", methods=["GET"])
def getSave():
    content = request.json
    cond = ["user_id"]
    result = checkParm(cond, content)
    if(result == ""):
        return ret({"success": False, "message": result})
    else:
        return ret(proposalModel.getSave(content.user_id))


@proposalAPI.route("/save", methods=["POST"])
def save():
    content = request.json
    cond = ["user_id", "proposal_id"]
    result = checkParm(cond, content)
    if(result == ""):
        return ret({"success": False, "message": result})

    else:
        return ret(proposalModel.save(content.user_id, content.proposal_id))


@proposalAPI.route("/report", methods=["POST"])
def report():
    content = request.json
    cond = ["user_id", "rule_id", "message_id"]
    t = checkParm(cond, content)
    if(t == ""):
        return ret(proposalModel.report(content.user_id, content.rule_id, content.message_id, content.remark))
    else:
        return ret({"success": False, "message": t})


@proposalAPI.route("/rule", methods=["GET"])
def rule():
    return ret(proposalModel.rule())


@proposalAPI.route("/cond", methods=["GET"])
def cond():
    return ret(proposalModel.getCond())
