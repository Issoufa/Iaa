#!/usr/bin/python
# -*- coding: utf-8 -*-

class Individu:
    def __init__(self, birth_day, name, first_name):
        self.birth_day = birth_day
        self.name = name
        self.first_name = first_name
        self.son = None
        self.daughter = None
        self.father = None
        self.mother = None

    def add_son(self, son_name, son_first_name, son_birth_day):
        pass

    def add_daughter(self, daughter_name, daughter_first_name, daughter_birth_day):
        pass

    def ddd(self):
        pass



if __name__ == "__main__":
    print("Local test script...")
    files_directory = "/home/abdou/Documents/PROJECT/PostDoc/graph/learnGNN/tests/"

    with open("product.json", "r") as fp:
        Product_dict = json.load(fp=fp)

    with open("lm_6544.json", "r") as fp:
        LM_dict = json.load(fp=fp)

    product = Product(**Product_dict)
    # Initiate product elements dict
    dict_el = {}
    for el in product.elements:
        dict_el[el.name] = el

    # data_test = data_examples(dict_el)
    #
    # data_lm = data_test["test_mai"]
    lm = LearningModule(**LM_dict)


    gg = GraphGenerator(product=product)
    # g_lm = gg.create_lm_graph(obj=lm)
    #
    # file_name = files_directory + "lm_graph_init_"
    # filename = filename_define(file_name)
    # graph_draw(g_lm, vertex_text=g_lm.vp.label, vertex_size=30, output_size=(1400, 1400), edge_pen_width=8,
    #            pos=sfdp_layout(g_lm), output=filename)

    # Generate dependence dict and the constraint id dict
    dict_depend, dict_const = gg.extract_opt_metat_const(obj=lm)
    g_support, dict_move_to = gg.create_support_graph(obj=lm, dict_depend=dict_depend, dict_const=dict_const)

    file_name = files_directory + "support_graph_init_"
    filename = filename_define(file_name)
    graph_draw(g_support, vertex_text=g_support.vp.label, vertex_size=30, output_size=(1400, 1400), edge_pen_width=8,
               pos=sfdp_layout(g_support), output=filename)
    print(" ici   1")
    set_qp_nodes, set_qp_sc_edges_out = generate_qp_sets_nodes_edges(
            g=g_support, dict_const=dict_const, dict_move_to= dict_move_to, file_directory=files_directory)

    print(" ici   2")
    set_qp_nodes_conditions, set_qp_out_interval = generate_qp_condition_score_interval(
            g=g_support,set_qp_nodes=set_qp_nodes, set_qp_sc_edges_out=set_qp_sc_edges_out,
            file_directory=files_directory)

    for qp_node in set_qp_nodes_conditions:
        print(f" qp in = {g_support.vp.label[qp_node[0]]}, node_out = {g_support.vp.label[qp_node[1]]}, interv = {set_qp_nodes_conditions[qp_node]}")
    for qp in set_qp_out_interval:
        print(f" {g_support.vp.label[qp]},  interval = {set_qp_out_interval[qp]}")

    fgggg =hhhjj
    # ==============================================================================================
    # ==============================================================================================
    # product_number_elements = 30
    # qp_proportion = random.uniform(0.4, 0.6)
    #
    # # generate production elements
    # dict_el = generate_product_elements(product_number_elements, qp_proportion)
    # # generate product
    # product = Product(id="564", name='Formation en communication verbale', type=ProductType.PRODUCT,
    #                   elements=[dict_el[el_name] for el_name in dict_el], keywords=[])
    #
    # data_test = data_examples(dict_el)
    #
    # data_lm = data_test["data1"]
    # product = Product(**data_test["product"])
    # data_lm = data_test["lm"]

    # Test data illuxi
    # data_test = data_examples()
    # product = Product(**data_test["p_illuxi"])
    # data_lm = data_test["lm_illuxi"]
    # lm_init_information = {"id": 65,
    #                 "name": "learning module test",
    #                 "product_id": 56,
    #                 "type": "learning_module",
    #                 "prerequisite": {},
    #                 "additional": []}
    # # Generation data for LM
    # lm_data = generate_lm(lm_init_information, product_number_elements, dict_el)
    #
    # gg = GraphGenerator(product=product)
    # lm = LearningModule(**data_lm)

    # v_prop_filter = "filter_bool"
    # e_prop_filter = "filter_bool"
    # for index_v in g_support.vertices():
    #     g_support.vp.filter_bool[index_v] = False
    # for e in g_support.edges():
    #     g_support.ep.filter_bool[e] = False
    #
    # for label_v in  result_opt[TypeOptOutput.DEP]:
    #     index_v = g_support.gp.id_to_vertex_map[label_v]
    #     g_support.vp.filter_bool[index_v] = True
    #
    # for i in range(1, len(result_opt[TypeOptOutput.DEP])):
    #     index_u = g_support.gp.id_to_vertex_map[result_opt[TypeOptOutput.DEP][i-1]]
    #     index_v = g_support.gp.id_to_vertex_map[result_opt[TypeOptOutput.DEP][i]]
    #     e = g_support.edge(index_u, index_v)
    #     g_support.ep.filter_bool[e] = True
    #
    # file_name = files_directory + "support_graph_sol_"
    # filename = filename_define(file_name)
    #
    # draw_graph_color(g=g_support, v_prop_filter=v_prop_filter, e_prop_filter=e_prop_filter, output_file_name = filename)
    #
    # print("=" * 40)
    # print(result_opt[TypeOptOutput.DEP])
    # print("=" * 40)
    # print(result_opt[TypeOptOutput.RIGHT])
    # print("+"*40)
    # print(result_opt[TypeOptOutput.SCORE])
    # print("=" * 40)
    #
    # =============================  DEBUT TESTS =====================================================================
    lm_vertex_id, end_node = "start", "end"
    lp = LearningPath(type=LearningPathType.LEARNING_PATH)
    historical_context = HistoricalContext(type=HistoricalContextType.USER_SESSION)
    learning_module_optimization_config = LMOptimizationConfig(
        type=LMOptimizationConfigType, optimization_factor=10, learning_factor=5, fun_factor=0)

    while lm_vertex_id != end_node:
        objective_value, duration, qp_score = 0, 0, 0
        qp_number_right_answers = 0
        element_type_value = None
        last_time = 10
        next_moves = NextMoves()

        if lm_vertex_id == "start":
            sg_vertex_id = lm_vertex_id
            historical_context.chosen_nodes[lm_vertex_id] = (0, 0, 0, 0, 0)  # score = 0, duration = 0
            historical_context.next_moves_dict[sg_vertex_id] = []

        else:
            if len(learning_path.path) == 1:
                previous_sg_vertex_id = "start"
            else:
                previous_sg_vertex_id = historical_context.support_learning_path[-2]

            # find vertex_id correspondence in next_moves set
            sg_vertex_id = historical_context.support_learning_path[-1]
            historical_context.next_moves_dict[sg_vertex_id] = []
            if previous_sg_vertex_id != "start":
                previous_lm_vertex_id = learning_path.path[-2]
                duration = 8 * 60
                objective_value = 1451.0
                qp_number_right_answers, qp_score = 0, 0
                for element in [el for el in product.elements if el.name == previous_lm_vertex_id]:
                    if element.type == ElementType.QUESTION_POOL:  # original qp
                        # begin process repeat, move_to or follow
                        qp = element.question_pool
                        qp_type = qp.type
                        question_indices = [0]  #
                        answer_choices = [[0, 0]]
                        if qp_type == QuestionPoolType.NBR_QUESTION_POOL:
                            qp_number_right_answers = qp.run(question_indices=question_indices, choices=answer_choices)

                        elif qp_type == QuestionPoolType.SUM_QUESTION_POOL:
                            qp_number_right_answers, qp_score = qp.run(
                                question_indices=question_indices, choices=answer_choices)

                    historical_context.chosen_nodes[previous_sg_vertex_id] = (
                        objective_score, duration, number_right_answers, total_score, element.type.value)

        next_moves = NextMoves()
        self.next_moves_keeper.set_session_next_moves(session_id=session_id, next_moves=next_moves)

        quick_optimize_next_moves(
            lm_vertex_id=lm_vertex_id,
            sg_vertex_id=sg_vertex_id,
            learning_module=lm,
            support_graph=g_support,
            learning_path=lp,
            next_moves=next_moves,
            historical_context=historical_context,
        )

        result = _optimize_next_moves(
            learning_module_=lm, sg_vertex_id=sg_vertex_id, learning_path=lp,
            historical_context=historical_context, g_support=g_support, dict_depend=dict_depend,
            dict_move_to=dict_move_to, dict_const=dict_const, next_moves=next_moves, timeout=last_time,
            files_directory_path=files_directory_path, lm_optimization_config=learning_module_optimization_config)

        if not result:
            print("optimization dont get solution")

        # choiced node number and define new actual_node
        num_choice = 0
        actual_node_index = next_moves.next_moves[num_choice][3]
        for index, n_score in enumerate(historical_context.next_moves_dict[sg_vertex_id]):
            if n_score[3] == actual_node_index:
                lm_vertex_id = n_score[1]
                new_sg_vertex_id = n_score[0]
                lp.add_node(new_vertex_id)
                historical_context.support_learning_path.append(new_sg_vertex_id)  # add the real label node
                break

        # historical_context.illuxi_path.append(list_send_to_illuxi[num_choice][0])   # add the real label node
        # historical_context.chosen_nodes[sg_vertex_id] = (list_send_to_illuxi[num_choice][1], -1)  # score , duration but the duration is know now
        # print(actual_node_ancestor)
        # if actual_node_ancestor not in ["start", "end"]:
        #     lp.add_node(actual_node_ancestor)
        # list_excluded = [vertex_label for vertex_label in historical_context.excluded_nodes]
        # last_time = round(100*(time() - time_init),2)   # update excluded list

    print("= " * 20)
    fffff = fgggg

    # =================================================================================================================
    print("LEARNING MODULE")
    # print(lm.cleaned_json())
    # Draw lm graph
    g1 = gg.create_lm_graph(obj=lm)
    file_name = files_directory + "lm_graph_"
    filename = filename_define(file_name)
    graph_draw(g1, vertex_text=g1.vp.label, vertex_size=30, output_size=(1400, 1400), edge_pen_width=8,
               pos=sfdp_layout(g1), output=filename)

    result_error = []
    # Generate dependence dict and the constraint id dict
    dict_depend, dict_const = gg.extract_opt_metat_const(obj=lm)

    # dict_const = correct_lm_qp_simulation(dict_const=dict_const, dict_element=dict_el)
